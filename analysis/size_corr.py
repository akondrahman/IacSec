'''
Size Correlation
Akond Rahman 
Jul 20, 2018 
'''
import pandas as pd
import numpy as np
from scipy import stats 
import cliffsDelta

def performCorr(file_name, mon_par):
    df_ = pd.read_csv(file_name)
    months = np.unique(df_['MONTH'].tolist())

    features = df_.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed: 12']
    smell_names = [x_ for x_ in features if x_ not in dropcols]

    for mon_ in months:
    	  if mon_== mon_par:
	    	  mon_df = df_[df_['MONTH']==mon_]
	    	  for smell_name in smell_names:
	    	  	  smell_count_list  = mon_df[smell_name].tolist()
	    	  	  file_name_list = np.unique(mon_df['FILE_NAME'].tolist())
	    	  	  file_size_list = [sum(1 for line_ in file_) for file_ in file_name_list]

	    	  	  corr_, p_value = stats.spearmanr(smell_count_list, file_size_list)
	    	  	  print '*'*50
	    	  	  print 'Smell:{},Spearman:{},p-val:{}'.format(smell_name, corr_, p_value)
	    	  	  print '*'*50
        

def performStatCompa(file_name, mon_par):
    df_ = pd.read_csv(file_name)
    print df_.head
    months = np.unique(df_['MONTH'].tolist())

    features = df_.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed: 12']
    smell_names = [x_ for x_ in features if x_ not in dropcols]

    for mon_ in months:
        if mon_== mon_par:
          mon_df = df_[df_['MONTH']==mon_]
          for smell_name in smell_names:
              smelly_files = np.unique(mon_df[mon_df[smell_name] > 0]['FILE_NAME'].tolist())
              non_smelly_files = np.unique(mon_df[mon_df[smell_name] <= 0]['FILE_NAME'].tolist())              

              smelly_loc_list     = [sum(1 for line_ in file_) for file_ in smelly_files]
              non_smelly_loc_list = [sum(1 for line_ in file_) for file_ in non_smelly_files]

              print '='*50
              print "Smelly Size [MEDIAN]:{}, [MEAN]:{}".format(np.median(smelly_loc_list), np.mean(smelly_loc_list))
              print "Non Smelly Size [MEDIAN]:{}, [MEAN]:{}".format(np.median(non_smelly_loc_list), np.mean(non_smelly_loc_list))
              if (np.mean(smelly_loc_list) != np.mean(non_smelly_loc_list)):
                 TS, p = stats.mannwhitneyu(smelly_loc_list, non_smelly_loc_list, alternative='greater')
              else:
                 TS, p = 0.0, 1.0
              cliffs_delta = cliffsDelta.cliffsDelta(smelly_loc_list, non_smelly_loc_list)
              print 'Feature:{}, pee value:{}, cliffs:{}'.format(smell_name, p, cliffs_delta)              
              print '='*50              

if __name__=='__main__':
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_GITHUB_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_MOZILLA_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_OPENSTACK_PUPPET.csv'
   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_WIKIMEDIA_PUPPET.csv'
   month = '2018-06'

   #performCorr(results_file, month)
   performStatCompa(results_file, month)
   print 'Dataset:', results_file