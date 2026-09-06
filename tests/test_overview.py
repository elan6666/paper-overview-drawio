"""Regression checks for the optional compiler, not an aesthetic benchmark."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("overview", ROOT / "scripts/overview.py")
overview = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(overview)


class OverviewTests(unittest.TestCase):
    def setUp(self):
        examples = ROOT / "assets/examples"
        self.contract = json.loads((examples / "paper-contract.json").read_text())
        self.scenes = [json.loads((examples / f"version-{i}.scene.json").read_text()) for i in (1, 2, 3)]

    def test_library_external_style_builds_native_source(self):
        self.scenes[2]["style_id"] = "FREE-biological-stage"
        selection = {"selected_styles": [s["style_id"] for s in self.scenes]}
        self.assertEqual(overview.compare(self.contract, selection, self.scenes)["status"], "pass")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "free.drawio"
            overview.compile_scene(self.contract, self.scenes[2], output)
            cells = ET.parse(output).findall(".//mxCell")
            self.assertEqual(len([c for c in cells if c.get("edge") == "1"]), 8)
            self.assertTrue(any(c.get("value") == "Add" for c in cells))

    def test_difference_count_is_advisory(self):
        scenes = [copy.deepcopy(self.scenes[0]) for _ in range(3)]
        scenes[2]["style_id"] = "FREE-test"
        result = overview.compare(self.contract, {"selected_styles": [s["style_id"] for s in scenes]}, scenes)
        self.assertEqual(result["status"], "pass")
        self.assertTrue(all(pair["same_geometry"] for pair in result["pairs"]))
        self.assertTrue(all(pair["review_note"] for pair in result["pairs"]))

    def test_missing_scientific_relation_is_detected(self):
        self.scenes[0]["edges"].pop()
        with self.assertRaisesRegex(ValueError, "Missing semantic edges"):
            overview.validate(self.contract, self.scenes[0])

    def test_reversed_scientific_relation_is_detected(self):
        edge = self.scenes[0]["edges"][0]
        edge["source"], edge["target"] = edge["target"], edge["source"]
        with self.assertRaisesRegex(ValueError, "direction/endpoints"):
            overview.validate(self.contract, self.scenes[0])


if __name__ == "__main__":
    unittest.main()
