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

def processPickle(pkl_p):



if __name__=='__main__':
   orig_csv = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_CDAT_CHEF.csv'
   ds_pkl = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_SYM_CDAT.PKL'

   orig_df = pandas.read_csv(orig_csv)
   pkl_lis = pickle.load(open(ds_pkl, 'rb'))
   pkl_df  pd.DataFrame([x for x in pkl_lis], columns=['MONTH', 'FILE_PATH', 'TYPE', 'CONTENT'])

   processPickle(pkl_df)
