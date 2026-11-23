import pathlib, yaml
def load_template(path):
    return yaml.safe_load(pathlib.Path(path).read_text())
def matches(template, app):
    req=template["http"][0]; path=req["path"][0]
    resp=app.get(path)
    for m in req.get("matchers",[]):
        if m["type"]=="status" and resp["status"] not in m["status"]: return False
        if m["type"]=="word" and not any(w in resp["body"] for w in m["words"]): return False
    return True
def validate_all(templates_dir, app):
    return {p.stem: matches(load_template(p), app) for p in sorted(pathlib.Path(templates_dir).glob("*.yaml"))}
