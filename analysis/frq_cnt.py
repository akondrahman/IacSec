'''
Akond Rahman
Smell count per script
Mar 17, 2018
'''
import pandas as pd
import numpy as np

def perfAnal(df_pa, header_pa):
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    for mon_ in mon_lis:
        for head_ in header_pa:
            mon_df = df_pa[df_pa['MONTH']==mon_]
            per_mon_cnt = sum(mon_df[head_].tolist()) # we need the total count
            per_mon_fil = np.unique(mon_df['FILE_NAME'].tolist())
            per_mon_fil_cnt = len(per_mon_fil)
            cnt_per_fil = float(per_mon_cnt)/float(per_mon_fil_cnt)
            print 'MON:{}, CNT:{}, FIL:{}, CNT_PER_FIL:{}, TYPE:{}'.format(mon_, per_mon_cnt, per_mon_fil_cnt, cnt_per_fil, head_)
            print '*'*25

if __name__=='__main__':
   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_TEST_PUPPET.csv'
   results_df   = pd.read_csv(results_file)
   '''
   pass the needed colun headers
   '''
   needed_header = ['HARD_CODE_SECR',	'SUSP_COMM',	'SECR_LOCA',	'MD5_USAG',
                    'HTTP_USAG',	'BIND_USAG',	'EMPT_PASS',	'DFLT_ADMN',
                    'BASE_64',	'MISS_DFLT',	'TOTAL']
   perfAnal(results_df, needed_header)
