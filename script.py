# Import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy import stats

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')

#1 - 
#print(abdata.head())
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
#print(Xtab)
chi2, pval, dof, expected = stats.chi2_contingency(Xtab)
print(pval)
print('Yes, there is significant differece')

#4 - 7
num_visitors = len(abdata)
#print(num_visitors)
num_sales_needed_099 = np.ceil(1000 / 0.99)
#print(num_sales_needed_099)
p_sales_needed_099 = (num_sales_needed_099 / num_visitors)  
print(p_sales_needed_099)

num_sales_needed_199 = np.ceil(1000 / 1.99)
#print(num_sales_needed_099)
p_sales_needed_199 = (num_sales_needed_199 / num_visitors)  
print(p_sales_needed_199)

num_sales_needed_499 = np.ceil(1000 / 4.99)
#print(num_sales_needed_099)
p_sales_needed_499 = (num_sales_needed_499 / num_visitors)  
print(p_sales_needed_499)

#8 -
samp_size_099 = np.sum(abdata.group == 'A')
#print(samp_size_099)
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
#print(sales_099)

pvalA = stats.binom_test(sales_099, n = samp_size_099, p = p_sales_needed_099, alternative = 'greater')
print(pvalA)

samp_size_199 = np.sum(abdata.group == 'B')
#print(samp_size_199)
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
#print(sales_199)

pvalB = stats.binom_test(sales_199, n = samp_size_199, p = p_sales_needed_199, alternative = 'greater')
print(pvalB)

samp_size_499 = np.sum(abdata.group == 'C')
#print(samp_size_499)
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))
#print(sales_499)

pvalC = stats.binom_test(sales_499, n = samp_size_499, p = p_sales_needed_499, alternative = 'greater')
print(pvalC)

print("based on calculations only Group C value is significant so, Brian should charge $4.99 for upgrade to meet the $1000 targets")