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

def processPickle(pkl_p):
    # print pkl_p.head()

    all_fil = np.unique(pkl_p['FILE_PATH'].tolist())
    all_sme = np.unique(pkl_p['TYPE'].tolist())
    all_sme = [getSmellName(x_) for x_ in all_sme]

    for file_name in all_fil:
        for smel in all_sme:
            per_fil_sme_df = pkl_p[file_name][smel]
            all_mon = np.unique(pkl_p['MONTH'].tolist())
            all_mon = sortDate(all_mon)
            for ind_ in xrange(len(all_mon)):
                fwd_ind = ind_ + 1
                if (fwd_ind < len(all_mon)):
                   curr_mon = all_mon[ind_]
                   next_mon = all_mon[fwd_ind]

                   mon_curr_df = per_fil_sme_df[curr_mon]
                   mon_next_df = per_fil_sme_df[next_mon]
                   curr_content_list = mon_curr_df['CONTENT'].tolist()
                   next_content_list = mon_next_df['CONTENT'].tolist()
                   print 'current month:{}, next month:{}, current list:{}, next list:{}'.format(curr_mon, next_mon, curr_content_list, next_content_list)

if __name__=='__main__':
   orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_CDAT_CHEF.csv'
   ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_CDAT.PKL'

   orig_df = pd.read_csv(orig_csv)
   pkl_lis = pickle.load(open(ds_pkl, 'rb'))
   pkl_df  = pd.DataFrame([x for x in pkl_lis], columns=['MONTH', 'FILE_PATH', 'TYPE', 'CONTENT'])

   processPickle(pkl_df)
