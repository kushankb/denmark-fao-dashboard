#!/usr/bin/env python3
"""Generate dashboard_data.js from Database_Denmark_dashboard 1.xlsx.

Schema (mirrors original dashboard):
domains[] -> name, actions[], total_actions, unique_policies, total_policies, total_metrics
  actions[] -> number, brief, long_description, policies[], metrics[], policy_count, metric_count
    policies[] -> description, long_description, policy_document, document_link,
                  document_year, linkage_type, instrument_type, page_number
    metrics[]  -> description, long_description, target, baseline, units, target_year,
                  baseline_year, policy_document, document_link, document_year, page_number
"""
import json, openpyxl, sys

SRC = "/Users/kushankbajaj/Downloads/Database_Denmark_dashboard 1.xlsx"
OUT = "dashboard_data.js"

wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)

def rows(name):
    r = list(wb[name].iter_rows(values_only=True))
    return r[1:]

def s(v):
    if v is None:
        return ""
    if isinstance(v, str):
        return v.strip()
    return v

def norm_domain(d):
    d = (d or "").strip()
    if d.rstrip(". ").lower() == "livestock":
        return "Livestock"
    return d

# ---- Policy Document lookup (by name) ----
pd_lookup = {}
for r in rows("Policy Document"):
    name = s(r[0])
    if not name:
        continue
    year = s(r[3])
    faolex = s(r[7])
    weblink = s(r[8])
    pd_lookup[name] = {
        "document_link": faolex or weblink,
        "document_year": year,
    }

# ---- Roadmap Actions backbone ----
# keyed by full description (col5) which is the join key used by the other sheets
DOMAIN_ORDER = ["Data", "Livestock", "Crops", "Fisheries and Aquaculture",
                "Soil and Water", "Forests and Wetlands", "Clean Energy",
                "Food Loss and Waste", "Enabling Healthy Diets for All",
                "Inclusive Policies"]

actions_by_full = {}   # full_desc -> action dict
domain_actions = {}    # domain name -> list of action dicts (in sheet order)

for r in rows("Roadmap Actions"):
    number = s(r[2])
    if not number:
        continue
    domain = norm_domain(r[0])
    full = s(r[5])
    action = {
        "number": number,
        "brief": s(r[3]),
        "long_description": full,
        "policies": [],
        "metrics": [],
        "policy_count": 0,
        "metric_count": 0,
    }
    actions_by_full[full] = action
    domain_actions.setdefault(domain, []).append(action)

# ---- Policy Actions -> policies ----
unmatched_pa = 0
for r in rows("Policy Actions"):
    desc = s(r[0])
    if not desc:
        continue
    link = s(r[4])  # roadmap full description
    action = actions_by_full.get(link)
    if action is None:
        unmatched_pa += 1
        continue
    doc = s(r[1])
    meta = pd_lookup.get(doc, {})
    action["policies"].append({
        "description": desc,
        "long_description": s(r[3]) or desc,
        "policy_document": doc,
        "document_link": meta.get("document_link", ""),
        "document_year": meta.get("document_year", ""),
        "linkage_type": s(r[7]),
        "instrument_type": s(r[8]),
        "page_number": s(r[2]),
    })

# ---- Metrics -> metrics ----
unmatched_m = 0
for r in rows("Metrics"):
    desc = s(r[0])
    if not desc:
        continue
    link = s(r[3])  # FAO roadmap action full description
    action = actions_by_full.get(link)
    if action is None:
        unmatched_m += 1
        continue
    doc = s(r[1])
    meta = pd_lookup.get(doc, {})
    action["metrics"].append({
        "description": desc,
        "long_description": s(r[5]) or desc,
        "target": s(r[6]),
        "baseline": s(r[7]),
        "units": s(r[8]),
        "target_year": s(r[10]),
        "baseline_year": s(r[11]),
        "policy_document": doc,
        "document_link": meta.get("document_link", ""),
        "document_year": meta.get("document_year", ""),
        "page_number": s(r[4]),
    })

# ---- Assemble domains ----
domains = []
present = [d for d in DOMAIN_ORDER if d in domain_actions]
# include any domain not in our predefined order, just in case
for d in domain_actions:
    if d not in present:
        present.append(d)

for dname in present:
    acts = domain_actions[dname]
    for a in acts:
        a["policy_count"] = len(a["policies"])
        a["metric_count"] = len(a["metrics"])
    total_policies = sum(a["policy_count"] for a in acts)
    total_metrics = sum(a["metric_count"] for a in acts)
    unique_docs = set()
    for a in acts:
        for p in a["policies"]:
            if p["policy_document"]:
                unique_docs.add(p["policy_document"])
    domains.append({
        "name": dname,
        "actions": acts,
        "total_actions": len(acts),
        "unique_policies": len(unique_docs),
        "total_policies": total_policies,
        "total_metrics": total_metrics,
    })

data = {"domains": domains}

with open(OUT, "w", encoding="utf-8") as f:
    f.write("window.dashboardData = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

# ---- Report ----
print(f"Wrote {OUT}")
print(f"Domains: {len(domains)}")
tot_a = sum(d['total_actions'] for d in domains)
tot_p = sum(d['total_policies'] for d in domains)
tot_m = sum(d['total_metrics'] for d in domains)
print(f"Actions: {tot_a} | Policy linkages: {tot_p} | Metrics: {tot_m}")
print(f"Unmatched policy actions: {unmatched_pa} | Unmatched metrics: {unmatched_m}")
for d in domains:
    print(f"   {d['name']:35} A={d['total_actions']:3} P={d['total_policies']:3} "
          f"uP={d['unique_policies']:3} M={d['total_metrics']:3}")
