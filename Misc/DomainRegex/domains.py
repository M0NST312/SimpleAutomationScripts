'''import csv

def load_domains_from_csv(file_path):
    domains = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            domain = row.get("domain")
            if domain:
                domains.append(domain.strip())
    return domains

def generate_regex(domains):
    escaped = [d.replace(".", "\\.") for d in domains]
    return "^[^@]+@(" + "|".join(escaped) + ")$"

if __name__ == "__main__":
    domains = load_domains_from_csv("domains.csv")
    regex = generate_regex(domains)
    with open("results.txt", "w") as f:
        f.write(regex)
    print(regex) 
'''
import csv
import json

def load_domains_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        return [row["domain"].strip() for row in csv.DictReader(f) if row.get("domain")]

def generate_regex(domains):
    escaped = [d.replace(".", "\\.") for d in domains]
    return "^[^@]+@(" + "|".join(escaped) + ")$"

domains = load_domains_from_csv("domains.csv")
regex = generate_regex(domains)

json_output = json.dumps({"regex": regex})
with open("results.txt", "w") as f:
    f.write(json_output)
print(json_output)