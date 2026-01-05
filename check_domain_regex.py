import json, re, sys

data = json.load(open("domain_regex.json"))
rules = data["rules"][0]["domain_regex"]

for r in rules:
    if not (r.startswith("^") and r.endswith("$")):
        sys.exit(f"Missing anchors: {r}")
    try:
        re.compile(r)
    except re.error as e:
        sys.exit(f"Invalid regex: {r}\n{e}")

print("domain_regex.json OK")
