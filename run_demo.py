import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lancepoint.fixture import FixtureApp
from lancepoint.matcher import validate_all
v=validate_all(pathlib.Path(__file__).parent/"templates", FixtureApp(patched=False))
p=validate_all(pathlib.Path(__file__).parent/"templates", FixtureApp(patched=True))
for k in v: print(f"{k}: vulnerable={v[k]} patched={p[k]}")
print(f"Templates: {len(v)}; fired on vulnerable: {sum(v.values())}; fired on patched: {sum(p.values())}")
