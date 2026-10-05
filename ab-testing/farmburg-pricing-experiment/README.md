# FarmBurg — Pricing Experiment Analysis

**Question:** FarmBurg (a farming-simulation game) tested an in-game upgrade at three price points — **$0.99 (A), $1.99 (B) and $4.99 (C)**. Which price should they charge to clear a **$1,000/week** revenue target?

## Approach
1. **Chi-square test of independence** — is purchase rate associated with price group?
2. **Break-even analysis** — for each price, compute the conversion rate needed to reach $1,000/week given typical weekly traffic.
3. **One-sided binomial tests** — is each group's observed conversion rate significantly *above* its break-even rate?

## Key insight
The $0.99 group had the highest purchase rate, so the naive conclusion is "charge $0.99". But a higher conversion rate is not the same as more revenue: only the **$4.99** price point was significantly above its break-even conversion rate, making it the recommended price.

## Run
```bash
python analysis.py   # expects data/clicks.csv (user_id, group, is_purchase)
```
