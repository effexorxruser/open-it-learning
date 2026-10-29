"""Research Batch #002 publication candidate contract tests.

Review metadata in staged catalog files reflects an independent public-source check,
not approval by the maintainer or a learner's award-delivery test.
"""
import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "journal" / "research-batch-002"
CARDS = FOLDER / "cards"
SCHEMA = json.loads((ROOT / "catalog/schema/course.schema.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
BLOCKED_ID = "one-c-future-code-element-2026"
STEP_THRESHOLDS = {
    "stepik-introduction-to-linux-73": (100, 113),
    "stepik-interactive-sql-63054": (136, 144),
    "stepik-yandex-cpp-363": (90, 106),
}
PREEXISTING_IDS = {
    "cs50-ai", "cs50-cybersecurity", "cs50-python", "cs50-sql", "cs50-web", "cs50-x",
    "freecodecamp-python-v9", "freecodecamp-responsive-web-design-v9",
    "openlearn-cyber-security", "openlearn-digital-skills", "openlearn-introducing-computing",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class Batch002Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proposals = {x["id"]: x for x in
                         [load(p) for p in CARDS.glob("*.json")]}
        cls.catalog = {x["id"]: x for x in
                       [load(p) for p in (ROOT / "catalog/verified").glob("*.json")]}
        cls.manifest = load(FOLDER / "batch.json")

    def test_new_and_existing_ids_and_urls_do_not_overlap(self):
        self.assertEqual(len(self.proposals), 11)
        self.assertEqual(len(self.catalog), 21)
        self.assertTrue(PREEXISTING_IDS.issubset(self.catalog))
        self.assertNotIn(BLOCKED_ID, self.catalog)
        self.assertEqual(set(self.proposals) - {BLOCKED_ID},
                         set(self.catalog) - PREEXISTING_IDS)
        all_urls = [c["official_url"].rstrip("/") for c in self.catalog.values()]
        self.assertEqual(len(all_urls), len(set(all_urls)))
        self.assertEqual(len({c["official_url"].rstrip("/") for c in self.proposals.values()}), 11)

    def test_staged_records_match_source_cards_without_approval_in_drafts(self):
        for record_id, record in self.proposals.items():
            with self.subTest(record=record_id):
                self.assertNotIn("review", record)
                self.assertTrue(list(VALIDATOR.iter_errors(record)))
                if record_id == BLOCKED_ID:
                    self.assertIsNone(record["outcomes"][0]["cost_to_obtain"])
                    projection = copy.deepcopy(record)
                    projection["review"] = {"status": "verified_free_outcome",
                                            "reviewed_at": self.manifest["editorial_review_checked_at"]}
                    self.assertTrue(list(VALIDATOR.iter_errors(projection)),
                                    "unknown price must remain non-publishable")
                    continue
                staged = self.catalog[record_id]
                expected = copy.deepcopy(record)
                expected["review"] = staged["review"]
                self.assertEqual(staged, expected)
                self.assertEqual(list(VALIDATOR.iter_errors(staged)), [])
                self.assertEqual(staged["review"]["status"], "verified_free_outcome")
                self.assertEqual(staged["review"]["reviewed_at"],
                                 self.manifest["editorial_review_checked_at"])

    def test_stepik_exact_public_api_thresholds(self):
        for record_id, (regular, distinction) in STEP_THRESHOLDS.items():
            with self.subTest(record=record_id):
                c = self.catalog[record_id]
                self.assertIn(f"{regular} баллов", c["outcomes"][0]["requirements"])
                self.assertIn(f"{distinction} баллов", c["outcomes"][0]["requirements"])
                api = "https://stepik.org/api/courses/" + record_id.split("-")[-1]
                self.assertTrue(any(e["source_url"] == api and
                                    e["short_quote"] == f'"certificate_regular_threshold": {regular}'
                                    for e in c["evidence"]))
                self.assertTrue(any(e["source_url"] == api and
                                    e["short_quote"] == '"is_certificate_auto_issued": true'
                                    for e in c["evidence"]))

    def test_source_coverage_and_russian_language(self):
        self.assertEqual(sum("ru" in c["languages"] for c in self.proposals.values()), 4)
        self.assertEqual(sum("ru" in c["languages"] for c in self.catalog.values()
                             if c["id"] not in PREEXISTING_IDS), 3)
        self.assertEqual(sum(len(c["evidence"]) for c in self.proposals.values()), 76)
        self.assertEqual(sum(len(c["outcomes"]) for c in self.catalog.values()), 27)
        for c in self.proposals.values():
            with self.subTest(record=c["id"]):
                self.assertGreaterEqual(len(c["evidence"]), 4)
                claims = {e["claim"] for e in c["evidence"]}
                self.assertIn("learning.free", claims)
                for i in range(len(c["outcomes"])):
                    for f in ("obtainable", "requirements", "cost_to_obtain"):
                        self.assertIn(f"outcomes[{i}].{f}", claims)
                for e in c["evidence"]:
                    self.assertTrue(e["source_url"].startswith("https://"))
                    self.assertGreaterEqual(len(e["short_quote"]), 2)
                    self.assertTrue(e["checked_at"].endswith("Z"))

    def test_extra_ceu_benefits_are_not_academic_credentials(self):
        for record_id, amount in [
            ("saylor-cs101-introduction-to-programming", 2.6),
            ("saylor-cs302-software-engineering", 3.6),
        ]:
            with self.subTest(record=record_id):
                c = self.catalog[record_id]
                self.assertEqual([x["type"] for x in c["outcomes"]],
                                 ["completion_certificate", "training_credit"])
                ceu = c["outcomes"][1]
                self.assertEqual(ceu["kind"], "benefit")
                self.assertIn(str(amount), ceu["name"])
                self.assertIn("not separate academic transfer credit", ceu["requirements"])
                self.assertEqual(ceu["cost_to_obtain"], 0)
                self.assertIsNone(ceu["currency"])

    def test_ibm_canonical_issuer_and_held_1c(self):
        badge = self.catalog["ibm-skillsbuild-ai-literacy"]["outcomes"][0]
        canonical = "https://www.credly.com/org/ibm-skillsbuild/badge/ai-literacy"
        self.assertEqual(badge["official_evidence_url"], canonical)
        self.assertEqual(badge["issuer"], "IBM SkillsBuild")
        one_c = self.proposals[BLOCKED_ID]
        self.assertIsNone(one_c["outcomes"][0]["cost_to_obtain"])
        self.assertIn("ОЧНОЙ", one_c["learning"]["conditions"])
        self.assertNotIn(BLOCKED_ID, self.catalog)

    def test_manifest_preserves_editorial_boundaries(self):
        self.assertEqual(self.manifest["batch_id"], "research-batch-002")
        self.assertFalse(self.manifest["catalog_publication_approved"])
        self.assertEqual(len(self.manifest["records"]), 11)
        self.assertEqual(sum(x["is_staged_in_catalog_pr"] for x in self.manifest["records"]), 10)
        self.assertEqual([x["status"] for x in self.manifest["records"]
                          if x["id"] == BLOCKED_ID], ["under_review"])


if __name__ == "__main__":
    unittest.main()
