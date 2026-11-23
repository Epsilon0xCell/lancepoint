import sys, unittest, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from lancepoint.fixture import FixtureApp
from lancepoint.matcher import validate_all, load_template
ROOT=pathlib.Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
    def test_six_templates(self): self.assertEqual(len(list((ROOT/"templates").glob("*.yaml"))),6)
    def test_all_fire_vulnerable_none_patched(self):
        v=validate_all(ROOT/"templates", FixtureApp(False)); p=validate_all(ROOT/"templates", FixtureApp(True))
        self.assertTrue(all(v.values())); self.assertFalse(any(p.values()))
    def test_template_shape(self):
        t=load_template(sorted((ROOT/"templates").glob("*.yaml"))[0]); self.assertIn("http", t); self.assertIn("info", t)
if __name__=="__main__": unittest.main()
