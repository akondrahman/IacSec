'''
Akond Rahman
Smell count per script
Mar 17, 2018
'''
import pandas as pd
import numpy as np

def perfAnal(df_pa):
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    for mon_ in mon_lis:
        mon_df = df_pa[df_pa['MONTH']==mon_]
        per_mon_cnt = mon_df['TOTAL'].tolist()
        per_mon_fil = np.unique(mon_df['FILE_NAME'].tolist())
        print 'MON:{}, CNT:{}, FIL:{}'.format(mon_, per_mon_cnt, per_mon_fil)
        print '*'*25

if __name__=='__main__':
   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_TEST_PUPPET.csv'
   results_df   = pd.read_csv(results_file)
   perfAnal(results_df)
