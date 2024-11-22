import pandas as pd
from scipy import stats

data = pd.read_csv('datasets/diabetes.csv')
sample = data['Glucose']
pop_mean = 100

t_stat, p_value = stats.ttest_1samp(sample, pop_mean)

print('T-statistic:', t_stat)
print('P-value:', p_value)

if p_value < 0.05:
    print('Reject null hypothesis')
else:
    print('Fail to reject null hypothesis')