import json
import unittest
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parent.parent

class TestJLM(unittest.TestCase):
    def test_synthetic_interventions_and_evaluations(self):
        s1 = json.loads((ROOT / "schemas/intervention_record.schema.json").read_text())
        for r in json.loads((ROOT / "data/synthetic/ds01_interventions.json").read_text()):
            jsonschema.validate(r, s1)
            self.assertEqual(r["publication_class"], "P5")
        s2 = json.loads((ROOT / "schemas/evaluation_record.schema.json").read_text())
        for r in json.loads((ROOT / "data/synthetic/ds02_evaluations.json").read_text()):
            jsonschema.validate(r, s2)
            self.assertFalse(r["causal_claim_permitted"])

if __name__ == "__main__":
    unittest.main()
