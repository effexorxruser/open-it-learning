"""Draft Batch #002: evidence structure and preservation of published-catalog boundary."""
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


def read_cards():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CARDS.glob("*.json"))]


class Batch002Checks(unittest.TestCase):
    def test_ten_distinct_drafts_outside_verified(self):
        records = read_cards()
        self.assertEqual(len(records), 10)
        self.assertEqual(len({x["id"] for x in records}), 10)
        urls = [x["official_url"].rstrip("/") for x in records]
        self.assertEqual(len(set(urls)), 10)
        published = [json.loads(path.read_text())
                     for path in (ROOT / "catalog/verified").glob("*.json")]
        self.assertEqual(len(published), 11)
        self.assertFalse(set(urls) & {x["official_url"].rstrip("/") for x in published})
        self.assertFalse({x["id"] for x in records} & {x["id"] for x in published})
        self.assertTrue(all("review" not in x for x in records))
        self.assertEqual(
            sum(len(x["outcomes"]) for x in published), 15,
            "research PR must not silently change published records")

    def test_russian_language_and_provider_diversity(self):
        records = read_cards()
        self.assertEqual(sum("ru" in x["languages"] for x in records), 4)
        providers = [x["provider"].lower() for x in records]
        expected_groups = ("1с-учебный", "stepik", "hp life", "saylor", "ibm", "microsoft", "kaggle")
        for group in expected_groups:
            self.assertTrue(any(group in p for p in providers), group)
        self.assertEqual(len(expected_groups), 7)

    def test_evidence_and_structure(self):
        cards = read_cards()
        self.assertEqual(sum(len(x["evidence"]) for x in cards), 50)
        for record in cards:
            with self.subTest(record=record["id"]):
                self.assertGreaterEqual(len(record["evidence"]), 4)
                self.assertEqual(len(record["outcomes"]), 1)
                self.assertEqual(record["learning"]["cost"], 0)
                self.assertIsNone(record["learning"]["currency"])
                self.assertTrue(list(VALIDATOR.iter_errors(record)),
                                "drafts without a review object must not be publishable")
                claims = {e["claim"] for e in record["evidence"]}
                for c in ("learning.free", "outcomes[0].obtainable",
                          "outcomes[0].cost_to_obtain", "outcomes[0].requirements"):
                    self.assertIn(c, claims)
                for e in record["evidence"]:
                    self.assertTrue(e["source_url"].startswith("https://"))
                    self.assertGreaterEqual(len(e["short_quote"]), 2)
                    self.assertGreaterEqual(len(e["review_note"]), 8)
                    self.assertTrue(e["checked_at"].endswith("Z"))

    def test_cost_uncertainty_never_becomes_zero(self):
        cards = {x["id"]: x for x in read_cards()}
        one_c = cards["one-c-future-code-element-2026"]
        self.assertIsNone(one_c["outcomes"][0]["cost_to_obtain"],
                          "missing issuance fee is unknown, not free")
        for key, record in cards.items():
            fake_review = copy.deepcopy(record)
            fake_review["review"] = {
                "status": "verified_free_outcome",
                "reviewed_at": "2026-10-29T15:05:00Z",
            }
            errors = list(VALIDATOR.iter_errors(fake_review))
            if key == "one-c-future-code-element-2026":
                self.assertTrue(errors, "unknown 1C issuance fee must block publication")
            else:
                self.assertEqual(errors, [], f"{key}: unexpected schema errors")

    def test_batch_manifest_unapproved(self):
        manifest = json.loads((FOLDER / "batch.json").read_text())
        self.assertEqual(manifest["batch_id"], "research-batch-002")
        self.assertFalse(manifest["catalog_publication_approved"])
        self.assertEqual(len(manifest["records"]), 10)
        status = {x["id"]: x["status"] for x in manifest["records"]}
        self.assertEqual(status["one-c-future-code-element-2026"], "under_review")
        self.assertEqual(sum("pending_threshold" in s for s in status.values()), 3)


if __name__ == "__main__":
    unittest.main()
