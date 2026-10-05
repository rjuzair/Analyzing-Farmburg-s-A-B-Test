# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

#1 - 5
print(dogs.head())
whippet_rescue = dogs.is_rescue[dogs.breed == 'whippet']
#print(whippet_rescue)
num_whippet_rescuses = np.count_nonzero(whippet_rescue)
print(num_whippet_rescuses)
num_whippets = len(whippet_rescue)
print(num_whippets)
pval = stats.binom_test(num_whippet_rescuses, num_whippets, 0.08)
print(pval)

#6 - 8
wt_whippets = dogs.weight[dogs.breed == 'whippet']
wt_terriers = dogs.weight[dogs.breed == 'terrier']
wt_pitbulls = dogs.weight[dogs.breed == 'pitbull']
#print(wt_terriers)
f_stats, pval = stats.f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)
results = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed)
print(results)
 #9 - 
Xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
print(Xtab)
chi2, pval, dof, expected = stats.chi2_contingency(Xtab)
print(pval)
