import re
import json

def convert_wildcards_to_regex(domain):
    # 将 '*' 替换为 '.*' 以匹配任意字符
    domain = domain.replace("*", ".*")

    # 修正正则表达式：确保可以匹配子域名和顶级域名
    domain = re.sub(r"([^.]+)\.([a-z]+)$", r"^\1(\.[^.]+)*\.\2$", domain)

    # 确保正则表达式以 ^ 开头，以 $ 结尾
    if not domain.startswith("^"):
        domain = "^" + domain
    if not domain.endswith("$"):
        domain = domain + "$"

    return domain

def generate_sing_box_rule(domains):
    # 生成 sing-box 规则文件
    return {"version": 3, "rules": [{"domain_regex": [convert_wildcards_to_regex(domain) for domain in domains]}]}

def read_wildcard_file(filename):
    # 读取 wildcard.txt 文件
    with open(filename, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]

def write_json_to_file(data, filename):
    # 写入 domain_regex.json 文件，覆盖原文件
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# 读取 wildcard.txt 文件
domains = read_wildcard_file("wildcard.txt")

# 生成 sing-box 规则文件
rules = generate_sing_box_rule(domains)

# 写入 domain_regex.json 文件，覆盖原文件
write_json_to_file(rules, "domain_regex.json")
