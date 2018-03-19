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
from dateutil import relativedelta

def createOutputDirectory(dirParam):
  if not os.path.exists(dirParam):
     os.makedirs(dirParam)

def sortDate(mon_lis):
    months = [datetime.datetime.strptime(m, "%Y-%m") for m in mon_lis]
    months.sort()
    sorted_mon = [datetime.datetime.strftime(m_, "%Y-%m") for m_ in months]
    return sorted_mon

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

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

def processPickleForNewOld(pkl_p, ori_p):
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

def getMonDiff(month_list):
    if len(month_list) > 1:
        month_list = [x_.replace(',', '') for x_ in month_list]
        sorted_months = sortDate(month_list)
        first = sorted_months[0]
        last  = sorted_months[-1]

        # print first, last
        first_year, first_mon = first.split('-')[0], first.split('-')[1]
        last_year, last_mon = last.split('-')[0], last.split('-')[1]
        # print first_year, first_mon
        date1 = datetime.datetime(int(first_year), int(first_mon), 1)
        date2 = datetime.datetime(int(last_year), int(last_mon), 1)

        r = relativedelta.relativedelta(date2, date1)
        dur_mon = r.months + r.years * 12
    else:
        dur_mon = 1
    return dur_mon

def processLifetimeData(pkl_p):

    str_ = ''
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
            content_list = np.unique(per_fil_sme_df['CONTENT'].tolist())
            for content in content_list:
                per_content_df=per_fil_sme_df[per_fil_sme_df['CONTENT']==content]
                mon_list = per_content_df['MONTH'].tolist()
                mon_dur=getMonDiff(mon_list)
                # print file_name, smel, content, mon_list, mon_dur
                str_ = str_ + file_name + ',' + smel + ',' + str(mon_dur) + ',' + '\n'
                print '='*50


    return str_

'''
ANALYZING ZONE
'''

def makePlot(x_par, y_par, head_par, out_dir_par, type_par, ds_par):
    plt_x_axis = [x_ for x_ in xrange(len(x_par))]
    plt.xticks(plt_x_axis, x_par)
    plt.plot(plt_x_axis, y_par)
    plt.title(head_par)
    plt.ylim(0.0, 1.25)
    plt.xlabel('MONTH')
    plt.ylabel(type_par)
    #plt.show()
    file2save = out_dir_par + head_par + '_' + type_par + '_' + ds_par + '.png'
    plt.savefig(file2save)
    plt.close()

def perfAnal(df_pa, header_pa, output_dir, ds_name):
    createOutputDirectory(output_dir)
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    mon_lis = sortDate(mon_lis)
    for head_ in header_pa:
        print head_
        smell_df = df_pa[df_pa['TYPE']==head_]
        mon_plt_lis, new_plt_lis, old_plt_lis = [], [], []
        count, cols = smell_df.shape
        if count > 0:
            for mon_ in mon_lis:
                mon_df = smell_df[smell_df['MONTH']==mon_]
                old_cnt = mon_df['OLD_CNT'].tolist()
                new_cnt = mon_df['NEW_CNT'].tolist()
                tot_cnt = mon_df['TOT_CNT'].tolist()
                all_cnt = sum(tot_cnt)
                # print old_cnt, new_cnt, tot_cnt
                if all_cnt <= 0:
                   all_cnt = all_cnt + 1
                old_pro = round(float(sum(old_cnt))/float(all_cnt), 3)
                new_pro = round(float(sum(new_cnt))/float(all_cnt), 3)
                mon_plt_lis.append(mon_)
                old_plt_lis.append(old_pro)
                new_plt_lis.append(new_pro)
                # print '*'*25
            makePlot(mon_plt_lis, old_plt_lis, head_, output_dir, 'OLD_PROPORTION', ds_name)
            makePlot(mon_plt_lis, new_plt_lis, head_, output_dir, 'NEW_PROPORTION', ds_name)
            print '='*50



if __name__=='__main__':

   '''
   pass the needed colun headers
   '''
   needed_header = ['HARD_CODE_SECR',	'SUSP_COMM',	'SECR_LOCA',	'MD5_USAG',
                    'HTTP_USAG',	'BIND_USAG',	'EMPT_PASS',	'DFLT_ADMN',
                    'BASE_64',	'MISS_DFLT']

   orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_BERG_CHEF.csv'
   ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_BERG.PKL'
   dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_berg/'
   name = 'BLOOMBERG'
   lifetime_out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_berg/LIFETIME.csv'

   # orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_CDAT_CHEF.csv'
   # ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_CDAT.PKL'
   # dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_cdat/'
   # name = 'CASKDATA'

   # orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_EXPR_CHEF.csv'
   # ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_EXPR.PKL'
   # dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_expr/'
   # name = 'EXPRESS42'

   # orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_MOZILLA_PUPPET.csv'
   # ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_ALL_MOZ.PKL'
   # dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_moz/'
   # name = 'MOZILLA'

   # orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_OPENSTACK_PUPPET.csv'
   # ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_ALL_OST_PUP.PKL'
   # dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_ost/'
   # name = 'OPENSTACK'

   # orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_WIKIMEDIA_PUPPET.csv'
   # ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_ALL_WIK_PUP.PKL'
   # dir2dump = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_wik/'
   # name = 'WIKIMEDIA'

   orig_df = pd.read_csv(orig_csv)
   pkl_lis = pickle.load(open(ds_pkl, 'rb'))
   pkl_df  = pd.DataFrame([x for x in pkl_lis], columns=['MONTH', 'FILE_PATH', 'TYPE', 'CONTENT'])
   '''
   OLD AND NEW ANALYSIS
   '''
   # df_old_new = processPickleForNewOld(pkl_df, orig_df)
   # # print df_old_new.head()
   # perfAnal(df_old_new, needed_header, dir2dump, name)
   '''
   life time analysis
   '''
   lifetime_str = processLifetimeData(pkl_df)
   print lifetime_str
   print '*'*100
   by = dumpContentIntoFile(lifetime_str, lifetime_out_file)
   print 'Dumped a file of {} bytes'.format(by)
