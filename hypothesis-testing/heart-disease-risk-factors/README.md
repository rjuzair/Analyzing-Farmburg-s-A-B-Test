# Heart Disease Research II — Risk Factors

Data: patients evaluated for heart disease at the Cleveland Clinic Foundation ([UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)).

| Question | Method |
|---|---|
| Is maximum heart rate (`thalach`) different for patients with heart disease? | Box plot + two-sample t-test |
| Is age different for patients with heart disease? | Box plot + two-sample t-test |
| Does max heart rate differ across chest-pain types? Which pairs? | One-way ANOVA + Tukey HSD |
| Is chest-pain type associated with a heart disease diagnosis? | Chi-square test of independence |

## Key insight
Patients diagnosed with heart disease had a significantly **lower maximum heart rate** than those without it.

## Run
```bash
python analysis.py   # expects data/heart_disease.csv
```
