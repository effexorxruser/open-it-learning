"""Batch #002 research proposal contract checks (no publication approval)."""
import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BATCH = json.loads((ROOT / "journal/research-batch-002/proposals.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "catalog/schema/course.schema.json").read_text(encoding="utf-8"))

class ResearchBatch002Tests(unittest.TestCase):
    def setUp(self):
        self.validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

    def test_ten_unique_proposals_and_no_approval(self):
        self.assertFalse(BATCH["catalog_publication_approved"])
        self.assertEqual(len(BATCH["records"]), 10)
        self.assertEqual(len({r["id"] for r in BATCH["records"]}), 10)
        self.assertEqual(len({r["official_url"] for r in BATCH["records"]}), 10)
        for r in BATCH["records"]:
            self.assertNotIn("review", r)

    def test_schema_projection_is_only_a_shape_check(self):
        for r in BATCH["records"]:
            with self.subTest(id=r["id"]):
                self.assertTrue(list(self.validator.iter_errors(r)))  # No approval
                sample = copy.deepcopy(r)
                sample["review"] = {"status": "verified_free_outcome",
                                    "reviewed_at": BATCH["research_checked_at"]}
                self.validator.validate(sample)  # Shape, NOT editorial acceptance

    def test_ru_and_1c_are_included_with_caveats(self):
        ru = [r for r in BATCH["records"] if "ru" in r["languages"]]
        self.assertGreaterEqual(len(ru), 4)
        self.assertEqual(len([r for r in ru if "1c" in r["category"]]), 1)
        decisions = BATCH["editorial_decisions"]
        self.assertEqual(len(decisions), 10)
        self.assertEqual(sum(d["status"] == "under_review" for d in decisions.values()), 3)
        for r in ru:
            if r["id"].startswith("stepik-"):
                self.assertEqual(decisions[r["id"]]["status"], "under_review")
                self.assertIn("threshold", decisions[r["id"]]["reason"])

    def test_each_outcome_has_specific_evidence(self):
        for r in BATCH["records"]:
            with self.subTest(id=r["id"]):
                claim_paths = {e["claim"] for e in r["evidence"]}
                self.assertIn("learning.free", claim_paths)
                for suffix in ("obtainable", "requirements", "cost_to_obtain"):
                    self.assertIn("outcomes[0]."+suffix, claim_paths)
                self.assertEqual(r["learning"]["cost"], 0)
                self.assertIsNone(r["learning"]["currency"])
                self.assertEqual(r["outcomes"][0]["cost_to_obtain"], 0)
                for e in r["evidence"]:
                    self.assertTrue(e["source_url"].startswith("https://"))
                    self.assertGreater(len(e["review_note"]), 12)

if __name__ == "__main__":
    unittest.main()
