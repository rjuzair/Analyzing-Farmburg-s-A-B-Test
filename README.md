# Statistical Analysis & A/B Testing in Python

A collection of applied statistics case studies: designing and analysing **A/B tests**, and choosing the right **hypothesis test** for real business and health questions.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-4051B5)

## Projects

### A/B testing
| Project | Business question | Techniques |
|---|---|---|
| [FarmBurg pricing experiment](ab-testing/farmburg-pricing-experiment) | Which of three price points maximises the chance of hitting a revenue target? | Chi-square, break-even analysis, one-sided binomial tests |
| [Nosh Mish Mosh sample size](ab-testing/nosh-mish-mosh-sample-size) | How many visitors are needed to detect a revenue-justifying lift? | Baseline rate, MDE, power analysis |
| [ShoeFly ad campaign](ab-testing/shoefly-ad-campaign) | Which traffic source and ad creative perform best? | CTR funnels, pivot tables, day-of-week segmentation |

### Hypothesis testing
| Project | Question | Techniques |
|---|---|---|
| [Familiar subscription study](hypothesis-testing/familiar-blood-transfusion-study) | Do subscriptions affect lifespan and iron levels? | One/two-sample t-tests, chi-square |
| [FetchMaker dog breeds](hypothesis-testing/fetchmaker-dog-breed-analysis) | Rescue rates, weights and colours across breeds | Binomial test, ANOVA, Tukey HSD, chi-square |
| [Heart disease I](hypothesis-testing/heart-disease-cholesterol-and-blood-sugar) | Cholesterol and blood sugar vs clinical thresholds | One-sample t-tests, binomial test |
| [Heart disease II](hypothesis-testing/heart-disease-risk-factors) | Heart rate, age and chest-pain type as risk factors | t-tests, ANOVA, Tukey HSD, chi-square |
| [NBA trends](hypothesis-testing/nba-rivalry-and-home-advantage) | Rivalries, home advantage and forecast accuracy | Histograms, chi-square, Pearson correlation |

## Choosing the right test
| Data | Comparing | Test used |
|---|---|---|
| Numeric, 1 sample | Sample mean vs a known value | One-sample t-test |
| Numeric, 2 groups | Two means | Two-sample t-test |
| Numeric, 3+ groups | Several means | ANOVA → Tukey HSD |
| Binary, 1 sample | Proportion vs a known rate | Binomial test |
| Categorical × categorical | Association | Chi-square test |

## Getting started
```bash
pip install -r requirements.txt
cd hypothesis-testing/heart-disease-risk-factors
python analysis.py
```
Each project reads its dataset from a local `data/` folder. The datasets were provided by the [Codecademy](https://www.codecademy.com/) Data Science path and are not redistributed here.
