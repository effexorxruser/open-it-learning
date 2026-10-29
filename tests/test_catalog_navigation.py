"""Structural checks for the browsable v1 IT taxonomy and ordered editorial paths."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "catalog/navigation"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class NavigationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy = load(BASE / "taxonomy.json")
        cls.placements = load(BASE / "placements.json")
        cls.paths = load(BASE / "learning-paths.json")
        cls.relationships = load(BASE / "relationships.json")
        cls.courses = {r["id"]: r for r in
                       (load(p) for p in (ROOT / "catalog/verified").glob("*.json"))}
        cls.domains = cls.taxonomy["domains"]
        cls.specs = {s["id"]: d["id"]
                     for d in cls.domains for s in d["specializations"]}
        cls.records = cls.placements["records"]

    def test_version_and_unique_taxonomy_ids(self):
        for obj in (self.taxonomy, self.placements, self.paths, self.relationships):
            self.assertEqual(obj["version"], 1)
        ids = [d["id"] for d in self.domains]
        self.assertEqual(len(ids), len(set(ids)))
        all_specs = [s["id"] for d in self.domains for s in d["specializations"]]
        self.assertEqual(len(all_specs), len(set(all_specs)))
        self.assertEqual(len(all_specs), 14)
        self.assertEqual(len(ids), 6)
        for d in self.domains:
            self.assertTrue(d["specializations"])
            for record in [d, *d["specializations"]]:
                self.assertTrue(record["label"]["en"])
                self.assertTrue(record["label"]["ru"])

    def test_every_verified_course_classified_once(self):
        ids = [r["course_id"] for r in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(self.courses),
                         "Navigation must cover every and only verified JSON record")
        for record in self.records:
            with self.subTest(id=record["course_id"]):
                self.assertIn(record["primary_specialization"], self.specs)
                extras = record["additional_specializations"]
                self.assertEqual(len(extras), len(set(extras)))
                self.assertNotIn(record["primary_specialization"], extras)
                self.assertTrue(set(extras).issubset(self.specs))
                self.assertTrue(self.courses[record["course_id"]]["review"]["status"]
                                in ("verified_free_outcome", "verified_paid_outcome"))

    def test_domain_pages_cover_primary_and_additional_courses(self):
        for d in self.domains:
            page = BASE / "domains" / (d["id"] + ".md")
            self.assertTrue(page.exists(), page)
            body = page.read_text(encoding="utf-8")
            for sp in d["specializations"]:
                self.assertIn(sp["label"]["ru"], body)
                for course in self.records:
                    linked = (course["primary_specialization"] == sp["id"]
                              or sp["id"] in course["additional_specializations"])
                    if linked:
                        self.assertIn("../../verified/" + course["course_id"] + ".json", body)
        self.assertNotIn("one-c-future-code-element-2026",
                         {c["course_id"] for c in self.records})
        enterprise = (BASE / "domains/enterprise-it.md").read_text(encoding="utf-8")
        self.assertIn("research-batch-002/cards/one-c-future-code-element-2026.json",
                      enterprise)
        self.assertNotIn("verified/one-c-future-code-element-2026.json", enterprise)

    def test_ordered_paths_are_distinct_and_do_not_imply_prerequisites(self):
        items = self.paths["paths"]
        self.assertGreaterEqual(len(items), 6)
        names = [x["id"] for x in items]
        self.assertEqual(len(names), len(set(names)))
        self.assertIn("not a verified prerequisite", self.paths["disclaimer"])
        rendered = (BASE / "learning-paths.md").read_text(encoding="utf-8")
        self.assertIn("not formal prerequisites", rendered)
        for p in items:
            with self.subTest(path=p["id"]):
                self.assertGreaterEqual(len(p["course_ids"]), 2)
                self.assertEqual(len(p["course_ids"]), len(set(p["course_ids"])))
                self.assertTrue(set(p["course_ids"]).issubset(self.courses))
                self.assertTrue(p["label"]["ru"])
                previous = -1
                for cid in p["course_ids"]:
                    link = "../verified/" + cid + ".json"
                    current = rendered.find(link)
                    self.assertGreater(current, previous)
                    previous = current

    def test_related_links_are_valid_distinct_and_non_prerequisite(self):
        edges = self.relationships["relationships"]
        keys = []
        for e in edges:
            with self.subTest(pair=(e["from"], e["to"])):
                self.assertIn(e["type"], ("related", "alternative"))
                self.assertNotEqual(e["from"], e["to"])
                self.assertIn(e["from"], self.courses)
                self.assertIn(e["to"], self.courses)
                self.assertTrue(e["note"]["ru"])
                keys.append(tuple(sorted((e["from"], e["to"]))))
        self.assertEqual(len(keys), len(set(keys)))
        self.assertIn("not formal course prerequisites",
                      self.relationships["disclaimer"])

    def test_course_count_is_derived_from_actual_records(self):
        self.assertEqual(len(self.courses), 21)
        self.assertEqual(sum(len(x["outcomes"]) for x in self.courses.values()), 27)
        self.assertEqual(sum(
            sum(bool(self.specs[r["primary_specialization"]] == d["id"])
                for r in self.records) for d in self.domains), len(self.courses))
        index = (BASE / "README.md").read_text(encoding="utf-8")
        self.assertIn("21 verified course records", index)


if __name__ == "__main__":
    unittest.main()
