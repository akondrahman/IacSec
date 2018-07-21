'''
Size Correlation
Akond Rahman 
Jul 20, 2018 
'''
import pandas as pd
import numpy as np
from scipy import stats 

def performCorr(file_name):
    df_ = pd.read_csv(file_name)
    months = np.unique(df_['MONTH'].tolist())

    features = df_.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed']
    smell_names = [x_ for x_ in features if x_ not in dropcols]

    for mon_ in months:
    	  mon_df = df_[mon_]
    	  for smell_name in smell_names:
    	  	  smell_count_list  = mon_df[smell_name].tolist()
    	  	  file_name_list = np.unique(mon_df['FILE_NAME'].tolist())
    	  	  file_size_list = [sum(1 for line_ in file_) for file_ in file_name_list]

    	  	  corr_, p_value = stats.spearmanr(smell_count_list, file_size_list)
    	  	  print '*'*50
    	  	  print 'Smell:{},Spearman:{},p-val:{}'.format(smell_name, corr_, p_value)
    	  	  print '*'*50
        

if __name__=='__main__':
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_GITHUB_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_MOZILLA_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_OPENSTACK_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_WIKIMEDIA_PUPPET.csv'

   performCorr(results_file)