'''
get summary stats from datasets
Akond Rahman
April 30, 2019 
'''
from scipy import stats
import pandas as pd
import numpy as np
import cliffsDelta


def giveTimeStamp():
  import time, datetime
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

# github_file    = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_AUTHOR_ANSIBLE_DATASET_GHUB.csv'
# openstack_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_AUTHOR_ANSIBLE_DATASET_OSTK.csv' 

# github_file    = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_GHUB_AUHTOR_CHEF.csv'
# openstack_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_OSTK_AUHTOR_CHEF.csv'

dataset_files = [github_file, openstack_file]

print "Started at:", giveTimeStamp()
for dataset_file in dataset_files:
    name = dataset_file.split('/')[-1]
    print "Dataset:", name
    df2read = pd.read_csv(dataset_file)
    #print df2read.head()

    features = df2read.columns
    dropcols = ['REPO', 'FILE', 'SMELL_FLAG', 'SMELL_COUNT']
    features2see = [x_ for x_ in features if x_ not in dropcols]
    for feature_ in features2see:
           '''
           all data summary
           '''
           data_for_feature = df2read[feature_]
           median_, mean_, total_ = np.median(data_for_feature), np.mean(data_for_feature), sum(data_for_feature)
           print "Feature:{}, [ALL DATA] median:{}, mean:{}, sum:{}".format(feature_, median_, mean_, total_  )
           print '='*50
           defective_vals_for_feature     = df2read[df2read['SMELL_FLAG']==1][feature_]
           non_defective_vals_for_feature = df2read[df2read['SMELL_FLAG']==0][feature_]
           '''
           summary time
           '''
           print 'THE FEATURE IS:', feature_
           print '='*25
           print "Smelly file values [MEDIAN]:{}, [MEAN]:{}".format(np.median(list(defective_vals_for_feature)), np.mean(list(defective_vals_for_feature)))
           print "Non smelly values [MEDIAN]:{}, [MEAN]:{}".format(np.median(list(non_defective_vals_for_feature)), np.mean(list(non_defective_vals_for_feature)))
           
           if feature_=='OWNER_LINES':
              TS, p = stats.mannwhitneyu(list(non_defective_vals_for_feature), list(defective_vals_for_feature), alternative='greater')
           else:
              TS, p = stats.mannwhitneyu(list(defective_vals_for_feature), list(non_defective_vals_for_feature), alternative='greater')

           cliffs_delta = cliffsDelta.cliffsDelta(list(defective_vals_for_feature), list(non_defective_vals_for_feature))
           print 'Feature:{}, P:{}, cliffs:{}'.format(feature_, p, cliffs_delta)
           print '='*50
    print '*'*100
print "Ended at:", giveTimeStamp()