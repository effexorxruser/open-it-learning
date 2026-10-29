"""Human-friendly catalog tests: real provider links, synchronized Markdown and data."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "catalog/courses"
VERIFIED = ROOT / "catalog/verified"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class HumanCoursePagesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = {r["id"]: r for r in (load(p) for p in VERIFIED.glob("*.json"))}

    def test_generator_output_is_current(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/build_course_pages.py"), "--check"],
            cwd=ROOT, capture_output=True, text=True, timeout=15, check=False
        )
        self.assertEqual(result.returncode, 0,
                         f"Course pages must match canonical data:\n{result.stdout}\n{result.stderr}")

    def test_every_verified_course_has_readable_page_with_direct_link(self):
        pages = {p.stem: p for p in COURSES.glob("*.md") if p.name != "README.md"}
        self.assertEqual(set(pages), set(self.data))
        for ident, course in self.data.items():
            with self.subTest(course=ident):
                page = pages[ident].read_text(encoding="utf-8")
                self.assertIn("# " + course["title"], page)
                self.assertIn(
                    f"[Открыть курс на официальном сайте →]({course['official_url']})",
                    page
                )
                self.assertIn(course["provider"], page)
                self.assertIn(f"../verified/{ident}.json", page)
                self.assertIn(course["review"]["reviewed_at"][:10], page)
                self.assertIn(course["review"]["recheck_after"][:10], page)
                for result in course["outcomes"]:
                    self.assertIn(result["name"], page)
                    self.assertIn(result["official_evidence_url"], page)
                self.assertTrue(course["official_url"].startswith("https://"))

    def test_list_index_and_wiki_have_all_provider_links(self):
        index = (COURSES / "README.md").read_text(encoding="utf-8")
        wiki = (ROOT / "wiki-source/Courses.md").read_text(encoding="utf-8")
        self.assertEqual(len(self.data), 21)
        for ident, course in self.data.items():
            with self.subTest(course=ident):
                self.assertIn(f"]({ident}.md)", index)
                self.assertIn(f"[Открыть курс]({course['official_url']})", index)
                self.assertIn(f"[Открыть курс]({course['official_url']})", wiki)
                self.assertIn(f"/catalog/courses/{ident}.md)", wiki)

    def test_specializations_and_routes_link_to_readable_pages(self):
        nav = ROOT / "catalog/navigation"
        places = load(nav / "placements.json")["records"]
        taxonomy = load(nav / "taxonomy.json")["domains"]
        domains = {
            spec["id"]: domain["id"] for domain in taxonomy
            for spec in domain["specializations"]
        }
        for placement in places:
            ident = placement["course_id"]
            primary = domains[placement["primary_specialization"]]
            page = (nav / "domains" / f"{primary}.md").read_text(encoding="utf-8")
            self.assertIn(f"../../courses/{ident}.md", page)
            self.assertIn(f"[Открыть курс]({self.data[ident]['official_url']})", page)
        for path in ("learning-paths.md", "relationships.md"):
            text = (nav / path).read_text(encoding="utf-8")
            self.assertNotIn("../verified/", text)
            self.assertIn("../courses/", text)

    def test_technical_index_is_not_a_json_only_directory(self):
        index = (VERIFIED / "README.md").read_text(encoding="utf-8")
        self.assertIn("../courses/README.md", index)
        for ident, course in self.data.items():
            self.assertIn(f"../courses/{ident}.md", index)
            self.assertIn(f"[Открыть курс]({course['official_url']})", index)
            self.assertIn(f"[JSON]({ident}.json)", index)

    def test_ibm_link_is_direct_with_sso_disclosure(self):
        ident = "ibm-skillsbuild-ai-literacy"
        course = self.data[ident]
        self.assertEqual(
            course["official_url"],
            "https://skills.yourlearning.ibm.com/activity/PLAN-1C903152880C"
        )
        self.assertIn("авторизации", course["learning"]["conditions"])
        archived = load(ROOT / f"journal/research-batch-002/cards/{ident}.json")
        self.assertEqual(archived["official_url"], course["official_url"])
        manifest = load(ROOT / "journal/research-batch-002/batch.json")
        entry = next(x for x in manifest["records"] if x["id"] == ident)
        self.assertEqual(entry["primary_url"], course["official_url"])

    def test_unverified_1c_is_not_in_course_list(self):
        bad = "one-c-future-code-element-2026"
        self.assertNotIn(bad, self.data)
        self.assertFalse((COURSES / (bad + ".md")).exists())
        self.assertIn(
            "не включена в этот подтверждённый список",
            (COURSES / "README.md").read_text(encoding="utf-8")
        )


if __name__ == "__main__":
    unittest.main()
