'''
Akond Rahman
Mar 18, 2018
Old and new smells analysis
'''
import cPickle as pickle
import os
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

def sortDate(mon_lis):
    months = [datetime.datetime.strptime(m, "%Y-%m") for m in mon_lis]
    months.sort()
    sorted_mon = [datetime.datetime.strftime(m_, "%Y-%m") for m_ in months]
    return sorted_mon

def getSmellName(sme_nam):
    dict_ = {'SECURITY:::SUSPICOUS_COMMENTS:::':'SUSP_COMM',
             'SECURITY:::HARD_CODED_SECRET_':'HARD_CODE_SECR',
             'SECURITY:::EXPOSING_SECRET_LOCATION_':'SECR_LOCA',
             'SECURITY:::MD5:::':'MD5_USAG',
             'SECURITY:::HTTP:::':'HTTP_USAG',
             'SECURITY:::BINDING_TO_ALL:::':'BIND_USAG',
             'SECURITY:::EMPTY_PASSWORD:::':'EMPT_PASS',
             'SECURITY:::ADMIN_BY_DEFAULT:::':'DFLT_ADMN',
             'SECURITY:::BASE64:::':'BASE_64'
            }
    return dict_[sme_nam]

def processFileName(single_file_name):
    splitted_dir_name = single_file_name.split('/')[5]
    year  = splitted_dir_name.split('-')[-2]
    month = splitted_dir_name.split('-')[-1]
    str2del = '-' + year + '-' + month
    str2ret = single_file_name.replace(str2del, '')
    return str2ret

def getTotalCount(df_, file, smel, mont):
    # print mont
    file_df   = df_[df_['FILE_NAME']==file]
    mont_df   = file_df[file_df['MONTH']==mont]
    # print mont_df
    smel_name = getSmellName(smel)
    smel_     = mont_df[smel_name].tolist()
    # print smel_
    smel_cnt = smel_[0]
    return smel_cnt

'''
MINING DATA
'''

def processPickle(pkl_p, ori_p):
    full_results_list = []
    # print pkl_p.head()
    pkl_p['FLT_FIL'] = pkl_p['FILE_PATH'].apply(processFileName)
    all_fil = np.unique(pkl_p['FLT_FIL'].tolist())
    # print all_fil
    all_sme = np.unique(pkl_p['TYPE'].tolist())

    for file_name in all_fil:
        per_fil_df = pkl_p[pkl_p['FLT_FIL']==file_name]
        # print per_fil_df
        for smel in all_sme:
            per_fil_sme_df = per_fil_df[per_fil_df['TYPE']==smel]
            # print per_fil_sme_df.head()
            # print '*'*25
            per_fil_all_mon = np.unique(per_fil_sme_df['MONTH'].tolist())
            per_fil_all_mon = [y_.replace(",", "") for y_ in per_fil_all_mon]
            per_fil_all_mon = sortDate(per_fil_all_mon)
            # print per_fil_all_mon
            for ind_ in xrange(len(per_fil_all_mon)):
                fwd_ind = ind_ + 1
                if (fwd_ind < len(per_fil_all_mon)):
                       real_curr_mon = per_fil_all_mon[ind_]
                       curr_mon = real_curr_mon + ',' ## added , to handle pickle month format
                       real_nxt_mon = per_fil_all_mon[fwd_ind]
                       next_mon = real_nxt_mon + ','

                       mon_curr_df = per_fil_sme_df[per_fil_sme_df['MONTH']==curr_mon]
                       mon_next_df = per_fil_sme_df[per_fil_sme_df['MONTH']==next_mon]
                       curr_content_list = mon_curr_df['CONTENT'].tolist()
                       next_content_list = mon_next_df['CONTENT'].tolist()

                       file2search = list(np.unique(mon_next_df['FILE_PATH'].tolist()))[0]
                       # print file2search

                       old_cnt = len(list(set(next_content_list) & set(curr_content_list)))
                       tot_cnt = getTotalCount(ori_p, file2search, smel, real_nxt_mon)
                       new_cnt = tot_cnt - old_cnt
                       # print 'current month:{}, next month:{}, current list:{}, next list:{}'.format(curr_mon, next_mon, curr_content_list, next_content_list)
                       # print 'Month:{}, Old:{}, New:{}, Total:{}, Type:{}, File:{}'.format(next_mon, old_cnt, new_cnt, tot_cnt, smel, file_name)
                       # print '*'*25
                       full_results_list.append((real_nxt_mon, old_cnt, new_cnt, tot_cnt, getSmellName(smel)))
                       if ind_==0:
                          old_cnt = 0
                          tot_cnt = getTotalCount(ori_p, file2search, smel, real_nxt_mon)
                          new_cnt = tot_cnt - old_cnt
                          # print 'Month:={}, Old:={}, New:={}, Total:={}, Type:={}, File:={}'.format(curr_mon, old_cnt, new_cnt, tot_cnt, smel, file_name)
                          # print '*'*25
                          full_results_list.append((real_curr_mon, old_cnt, new_cnt, tot_cnt, getSmellName(smel)))

    # print full_results_list
    df2ret = pd.DataFrame.from_records(full_results_list, columns=['MONTH', 'OLD_CNT', 'NEW_CNT', 'TOT_CNT', 'TYPE'])
    return df2ret

'''
ANALYZING DATA
'''

def perfAnal(df_pa, header_pa, output_dir, ds_name):
    createOutputDirectory(output_dir)
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    mon_lis = sortDate(mon_lis)
    for head_ in header_pa:
        smell_df = df_pa[df_pa['TYPE']==head_]
        mon_plt_lis, new_plt_lis, old_den_lis = [], [], []
        for mon_ in mon_lis:
            mon_df = smell_df[smell_df['MONTH']==mon_]
            old_cnt = mon_df['OLD_CNT'].tolist()
            new_cnt = mon_df['NEW_CNT'].tolist()
            tot_cnt = mon_df['TOT_CNT'].tolist()
            print old_cnt, new_cnt, tot_cnt
            # mon_plt_lis.append(mon_)
            # cnt_plt_lis.append(cnt_per_fil)
            # sme_den_lis.append(smell_density)
            print '*'*25

        # makePlot(mon_plt_lis, cnt_plt_lis, head_, output_dir, 'CNT_PER_FIL', ds_name)
        # makePlot(mon_plt_lis, sme_den_lis, head_, output_dir, 'SMELL_DENSITY_KLOC', ds_name)
        print '='*50



if __name__=='__main__':
   orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_CDAT_CHEF.csv'
   ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_CDAT.PKL'
   dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_cdat/'
   name = 'CASKDATA'

   orig_df = pd.read_csv(orig_csv)
   pkl_lis = pickle.load(open(ds_pkl, 'rb'))
   pkl_df  = pd.DataFrame([x for x in pkl_lis], columns=['MONTH', 'FILE_PATH', 'TYPE', 'CONTENT'])

   df_old_new = processPickle(pkl_df, orig_df)
   # print df_old_new.head()

   '''
   pass the needed colun headers
   '''
   needed_header = ['HARD_CODE_SECR',	'SUSP_COMM',	'SECR_LOCA',	'MD5_USAG',
                    'HTTP_USAG',	'BIND_USAG',	'EMPT_PASS',	'DFLT_ADMN',
                    'BASE_64',	'MISS_DFLT']

   perfAnal(df_old_new, needed_header, dir2dump, name)
