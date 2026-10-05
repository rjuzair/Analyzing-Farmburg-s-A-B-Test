# Familiar — Blood-Transfusion Subscription Study

**Question:** Familiar sells two blood-transfusion subscriptions (Vein Pack and Artery Pack). Do they improve subscriber outcomes?

| Question | Test |
|---|---|
| Do Vein Pack subscribers live longer than the 73-year average? | One-sample t-test (one-sided) |
| Do Vein and Artery Pack lifespans differ? | Two-sample t-test |
| Is the pack associated with iron level (low/normal/high)? | Chi-square test of independence |

## Run
```bash
python analysis.py   # expects data/familiar_lifespan.csv and data/familiar_iron.csv
```
