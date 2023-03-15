# pip install scipy
from scipy import stats
import pandas as pd
ft2=pd.read_csv('weight.csv', index_col='id')
ft2_grp1 = ft2[ft2.group == 1]['weight']
ft2_grp2 = ft2[ft2.group == 2]['weight']
print()
print(stats.ttest_ind(ft2_grp1, ft2_grp2))

