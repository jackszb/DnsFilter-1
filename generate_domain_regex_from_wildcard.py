import re
import json

def convert_wildcards_to_regex(domain):
    domain = domain.replace("*", ".*")
    domain = re.sub(r"([^.]+)\.([a-z]+)$", r"^\1(\\.[^.]+)*\\.\\2$", domain)
    domain = re.sub(r"^\*", "^([^.]+\\.)*", domain)
    if not domain.startswith("^"):
        domain = "^" + domain
    if not domain.endswith("$"):
        domain = domain + "$"
    return domain

def generate_sing_box_rule(domains):
    return {"version": 3, "rules": [{"domain_regex": [convert_wildcards_to_regex(domain) for domain in domains]}]}

def read_wildcard_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

domains = read_wildcard_file("wildcard.txt")
rules = generate_sing_box_rule(domains)

with open("domain_regex.json", "w") as f:
    json.dump(rules, f, indent=2)
