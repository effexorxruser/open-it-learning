"""Behavioral contract tests for free/paid outcomes and draft research records."""
import copy
import json
import re
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / 'catalog/schema/course.schema.json').read_text())
EXAMPLE = json.loads(re.search(r'```json\n(.*?)\n```', (ROOT / 'docs/DATA_CONTRACT.md').read_text(), re.S)[1])

class CourseSchemaTests(unittest.TestCase):
    def setUp(self):
        self.validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
        self.record = copy.deepcopy(EXAMPLE)

    def valid(self, record):
        self.validator.validate(record)

    def invalid(self, record):
        self.assertTrue(list(self.validator.iter_errors(record)))

    def test_schema_and_existing_records_remain_valid(self):
        Draft202012Validator.check_schema(SCHEMA)
        self.valid(self.record)
        for path in (ROOT / 'catalog/verified').glob('*.json'):
            with self.subTest(record=path.name): self.valid(json.loads(path.read_text()))

    def test_free_prices_accept_unspecified_currency(self):
        self.record['learning']['currency'] = None
        self.record['outcomes'][0]['currency'] = None
        self.valid(self.record)

    def test_positive_price_needs_currency(self):
        self.record['review']['status'] = 'verified_paid_outcome'
        self.record['outcomes'][0]['cost_to_obtain'] = 25
        self.record['outcomes'][0]['currency'] = None
        self.invalid(self.record)
        self.record['outcomes'][0]['currency'] = 'EUR'
        self.valid(self.record)

    def test_unknown_price_is_not_free(self):
        self.record['outcomes'][0]['cost_to_obtain'] = None
        self.invalid(self.record)

    def test_missing_currency_is_not_the_same_as_explicit_null(self):
        del self.record['outcomes'][0]['currency']
        self.invalid(self.record)

    def test_malformed_currency_is_rejected(self):
        for bad in ['', 'usd', 'EURO', 0]:
            with self.subTest(currency=bad):
                self.record['outcomes'][0]['currency'] = bad
                self.invalid(self.record)

    def test_paid_and_free_statuses_cannot_be_swapped(self):
        self.record['review']['status'] = 'verified_paid_outcome'
        self.invalid(self.record)
        self.record['review']['status'] = 'verified_free_outcome'
        self.record['outcomes'][0]['cost_to_obtain'] = 1
        self.invalid(self.record)

    def test_unreviewed_record_is_not_publishable(self):
        del self.record['review']
        self.invalid(self.record)

    def test_batch_proposals_are_unapproved_but_have_valid_record_fields(self):
        bundle = json.loads((ROOT / 'journal/research-batch-001/proposals.json').read_text())
        self.assertFalse(bundle['catalog_publication_approved'])
        self.assertEqual(len(bundle['records']), 10)
        existing_urls = {json.loads(p.read_text())['official_url'].rstrip('/')
                         for p in (ROOT / 'catalog/verified').glob('*.json')}
        urls = set()
        ids = set()
        for record in bundle['records']:
            with self.subTest(record=record['id']):
                self.assertNotIn('review', record)  # Independent approval is deliberately absent.
                self.invalid(record)
                self.assertNotIn(record['id'], ids)
                ids.add(record['id'])
                url = record['official_url'].rstrip('/')
                self.assertNotIn(url, urls | existing_urls)
                urls.add(url)
                # In-memory projection tests shape only, not approval or truth.
                projected = copy.deepcopy(record)
                projected['review'] = {'status': 'verified_free_outcome',
                                       'reviewed_at': bundle['research_checked_at']}
                self.valid(projected)
                claims = {e['claim'] for e in record['evidence']}
                self.assertIn('learning.free', claims)
                for i in range(len(record['outcomes'])):
                    for field in ['obtainable', 'requirements', 'cost_to_obtain']:
                        self.assertIn(f'outcomes[{i}].{field}', claims)

    def test_dates_are_checked(self):
        self.record['evidence'][0]['checked_at'] = 'not-a-date'
        self.invalid(self.record)

if __name__ == '__main__': unittest.main()
