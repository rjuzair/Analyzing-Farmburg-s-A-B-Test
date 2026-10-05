# Nosh Mish Mosh — A/B Test Sample Size Planning

**Question:** A meal-kit company wants to test artisanal product photography. A new supplier is only worth it if the change brings in **$1,240+ extra revenue per week**. How many visitors must see each variant before the result can be trusted?

## Approach
- **Baseline conversion rate** from a week of visitor and purchase logs.
- **Minimum detectable effect (MDE)**: average order value → extra customers needed per week → required lift, expressed relative to the baseline.
- **Sample size** per variant via a power analysis for a two-proportion z-test (α = 0.10, power = 0.80) using `statsmodels`.

## Skills
Experiment design · statistical power · translating business targets into statistical parameters

## Run
```bash
python analysis.py   # requires the course-provided `noshmishmosh` data module
```
