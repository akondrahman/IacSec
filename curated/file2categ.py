'''
Akond Rahman
April 05, 2018
Thursday
This script maps each file to catgeory
'''
import pandas as pd
import csv
import numpy as np
import os
from shutil import copyfile

def getAPDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             apID = int(row[1])
             name = row[0]
             if apID not in dict_:
                 dict_[apID] = name
    return dict_

def getProDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             studentID = row[0]
             sweExp = row[1]
             iacExp = row[2]
             time   = row[3]
             if studentID not in dict_:
                 dict_[studentID] = ( sweExp, iacExp, time)
    return dict_

def getSubmDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             scriptID = row[0]
             apID = row[1]
             if scriptID not in dict_:
                 dict_[scriptID] = [apID]
             else:
                 dict_[scriptID] = [apID] + dict_[scriptID]
    return dict_

def getScriptPath(id_param, df_param):
    id_param = int(id_param)
    path2ret = df_param[df_param['scriptID']==id_param]['path'].tolist()[0]
    return path2ret

def getScriptContent(id_param, df_param):
    id_param = int(id_param)
    content = df_param[df_param['scriptID']==id_param]['content'].tolist()[0]
    return content

def getLabel(dic, inp):
    lab = ''
    inp = int(inp)
    if inp in dic:
        lab = dic[inp]
    return lab

def getAgreement(dict_pa, scr_df, dict_ap):
    agrCnt, disAgrCnt  = 0, 0
    lis2ret = []
    for k_, v_ in dict_pa.iteritems():
        scr_pat = getScriptPath(k_, scr_df)
        if (len(v_)==1):
            agrCnt += 1
            scr_lab = getLabel(dict_ap, v_[0])
            lis2ret.append((scr_pat, scr_lab))
        elif (len(np.unique(v_))==1):
            agrCnt += 1
            scr_lab = getLabel(dict_ap, np.unique(v_)[0])
            lis2ret.append((scr_pat, scr_lab))
        else:
            scr_lab = getLabel(dict_ap , str(np.bincount(v_).argmax()))
            scr_lab_occ = scr_lab.count(scr_lab)
            tot_len = len(v_)
            freq_perc  = float(scr_lab_occ)/float(tot_len)
            # if the most frequent is 50% of the list , then agreement
            if freq_perc >= 0.50:
                agrCnt += 1
                lis2ret.append((scr_pat, scr_lab))
            else:
                disAgrCnt += 1
                scr_con = getScriptContent(k_, scr_df)
                lis2ret.append((scr_pat, 'DISAGREED'))

    return lis2ret, agrCnt, disAgrCnt

def slicPreparation(cur_lis):
    ind_ = 0
    list4slic = []
    ### only agreed files and existing files will be copied, rest is determined by SLIC
    for tup_ in cur_lis:
        ind_ += 1
        file_name = tup_[0]
        ## we will move forward for only with PUPPET files
        if 'pp' in file_name:
            categ = tup_[1]
            if categ != 'DISAGREED':
                if (os.path.exists(file_name)):
                   copyfile(file_name, '/Users/akond/SECU_REPOS/curated/agreed/' + str(ind_) + '.pp')
                   list4slic.append(('AGREED', ind_, file_name, categ))
                else:
                   list4slic.append(('PATH_DO_NOT_EXIST', ind_, file_name, 'SLIC'))
            else:
                   copyfile(file_name, '/Users/akond/SECU_REPOS/curated/disagreed/' + str(ind_) + '.pp')
                   list4slic.append(('DISAGREED', ind_, file_name, 'SLIC'))
    return list4slic

if __name__=='__main__':
   apa_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/antipattern_table.csv'
   pro_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/profile_table.csv'
   scr_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/script_table.csv'
   sub_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/submission_table.csv'

   curated_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED.csv'

   '''
   get anti patterns
   '''
   ap_di = getAPDict(apa_tbl)
   # print ap_di
   '''
   get profile
   '''
   pr_di = getProDict(pro_tbl)
   # print pr_di
   '''
   get script table
   '''
   sc_df = pd.read_csv(scr_tbl)
   # print sc_df.head()
   '''
   get submissions
   '''
   sb_di = getSubmDict(sub_tbl)
   # print sb_di
   full_list, agrCnt, disAgrCnt = getAgreement(sb_di, sc_df, ap_di)
   print full_list
   print "Agreements:{}, disagreements:{}".format(agrCnt, disAgrCnt)
   '''
   once we have the full list , we need to copy the files so that SLIC can run
   the ones that are agreed upon by the raters, need to be checked , SLIC's decisions
   is final on the disagreed ones
   '''

   compare_ls=slicPreparation(full_list)
   curated_df = pd.DataFrame.from_records(compare_ls, columns=['TYPE', 'INDEX', 'PATH', 'SECU_LABEL'])
   curated_df.to_csv(curated_ds)
