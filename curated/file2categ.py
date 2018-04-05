'''
Akond Rahman
April 05, 2018
Thursday
This script maps each file to catgeory
'''
import pandas as pd
import csv

def getAPDict(file_):
    dict_ = {}
    with open(file_, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             apID = row[0]
             name = row[1]
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

if __name__=='__main__':
   apa_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/antipattern_table.csv'
   pro_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/profile_table.csv'
   scr_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/script_table.csv'
   sub_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/submission_table.csv'

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
   print sb_di
