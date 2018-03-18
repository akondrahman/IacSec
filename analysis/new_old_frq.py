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

def processPickle(pkl_p):
    # print pkl_p.head()
    pkl_p['FLT_FIL'] = pkl_p['FILE_PATH'].apply(processFileName)
    all_fil = np.unique(pkl_p['FLT_FIL'].tolist())
    # print all_fil
    all_sme = np.unique(pkl_p['TYPE'].tolist())

    for file_name in all_fil:
        per_fil_df = pkl_p[pkl_p['FILE_PATH']==file_name]
        print per_fil_df
        per_fil_all_mon = np.unique(per_fil_df['MONTH'].tolist())
        per_fil_all_mon = [y_.replace(",", "") for y_ in per_fil_all_mon]
        per_fil_all_mon = sortDate(per_fil_all_mon)

        # print per_fil_all_mon
        for ind_ in xrange(len(per_fil_all_mon)):
            fwd_ind = ind_ + 1
            if (fwd_ind < len(per_fil_all_mon)):
                   curr_mon = per_fil_all_mon[ind_]
                   next_mon = per_fil_all_mon[fwd_ind]

                   mon_curr_df = per_fil_sme_df[curr_mon]
                   mon_next_df = per_fil_sme_df[next_mon]
                   curr_content_list = mon_curr_df['CONTENT'].tolist()
                   next_content_list = mon_next_df['CONTENT'].tolist()
                   # print 'current month:{}, next month:{}, current list:{}, next list:{}'.format(curr_mon, next_mon, curr_content_list, next_content_list)

if __name__=='__main__':
   orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_CDAT_CHEF.csv'
   ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_CDAT.PKL'

   orig_df = pd.read_csv(orig_csv)
   pkl_lis = pickle.load(open(ds_pkl, 'rb'))
   pkl_df  = pd.DataFrame([x for x in pkl_lis], columns=['MONTH', 'FILE_PATH', 'TYPE', 'CONTENT'])

   processPickle(pkl_df)

        # for smel in all_sme:
        #     per_fil_sme_df = per_fil_df[per_fil_df['TYPE']==smel]
        #     print per_fil_sme_df
        #     print '*'*25
