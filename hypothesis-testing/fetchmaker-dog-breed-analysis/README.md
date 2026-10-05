# FetchMaker — Dog Breed Hypothesis Testing

**Context:** FetchMaker matches prospective owners with adoptable dogs. This analysis answers three product questions from their data.

| Question | Test |
|---|---|
| Are whippets more or less likely than the 8% average to be rescues? | Two-sided binomial test |
| Do whippets, terriers and pitbulls differ in average weight — and which pairs? | One-way ANOVA + Tukey HSD |
| Do poodles and shih tzus come in different colours? | Chi-square test of independence |

## Run
```bash
python analysis.py   # expects data/dog_data.csv
```
