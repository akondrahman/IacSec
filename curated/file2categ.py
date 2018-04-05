'''
Akond Rahman
April 05, 2018
Thursday
This script maps each file to catgeory
'''
import pandas as pd

if __name__=='__main__':
   apa_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/antipattern_table.csv'
   pro_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/profile_table.csv'
   scr_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/script_table.csv'
   sub_tbl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/submission_table.csv'

   '''
   get anti patterns
   '''
   ap_df = pd.read_csv(apa_tbl)
   # print ap_df.head()
   '''
   get profile
   '''
   pr_df = pd.read_csv(pro_tbl)
   # print pr_df.head()
   '''
   get script table
   '''
   sc_df = pd.read_csv(scr_tbl)
   print sc_df.head()
