'''
Akond Rahman
Smell count per script
Mar 17, 2018
'''
import pandas as pd
import numpy as np
import datetime

def calcSmellDensity(smell_cnt, file_list):
    val = 0
    tot_lin = 0
    for file_path in file_list:
        file_ = open(file_path, 'rU')
        num_lines = sum(1 for line_ in file_)
        tot_lin = tot_lin + num_lines
    val = float(smell_cnt)/float(tot_lin)
    return val

def sortDate(mon_lis):
    months = [datetime.datetime.strptime(m, "%Y-%m") for m in mon_lis]
    months.sort()
    sorted_mon = [datetime.datetime.strftime(m_, "%Y-%m") for m_ in months]
    return sorted_mon

def perfAnal(df_pa, header_pa):
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    mon_lis = sortDate(mon_lis)
    for head_ in header_pa:
        for mon_ in mon_lis:
            mon_df = df_pa[df_pa['MONTH']==mon_]
            per_mon_cnt = sum(mon_df[head_].tolist()) # we need the total count
            per_mon_fil = np.unique(mon_df['FILE_NAME'].tolist()) # we need the unique file names
            per_mon_fil_cnt = len(per_mon_fil) # unque file count
            cnt_per_fil   = float(per_mon_cnt)/float(per_mon_fil_cnt)
            smell_density = calcSmellDensity(per_mon_cnt, per_mon_fil)
            print 'MON:{}, CNT:{}, FIL:{}, CNT_PER_FIL:{}, SMELL_DENS:{}, TYPE:{}'.format(mon_, per_mon_cnt, per_mon_fil_cnt, cnt_per_fil, smell_density, head_)
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
