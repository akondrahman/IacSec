'''
Akond Rahman
Nov 15, 2017
Wednesday
Feature importance for IaC Metrics using RF
'''
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def readDataset(fileParam, dataTypeFlag=True):
  if dataTypeFlag:
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')
  return data_set_to_return

def getColumnNames(file_name_param, col_indicies2del):
    ds_   = pd.read_csv(file_name_param)
    temp_ = list(my_dataframe.columns.values)
    for col_ in col_indicies2del:
        del temp_[-col_]
    return temp_

def calcFeatureImp(feature_vec, label_vec):
    theRndForestModel = RandomForestClassifier()
    theRndForestModel.fit(feature_vec, label_vec)
    feat_imp_vector=theRndForestModel.feature_importances_
    print feat_imp_vector
    #for imp_vec in feat_imp_vector:


if __name__=='__main__':
   ds_file_name = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_BASTION_FULL_PROCESS_DATASET.csv'



   full_ds=readDataset(ds_file_name)
   full_rows, full_cols = np.shape(full_ds)
   feature_cols = full_cols - 1
   all_features = full_ds[:, 2:feature_cols]
   all_labels  =  full_ds[:, feature_cols]
   defected_file_count     = len([x_ for x_ in all_labels if x_==1.0])
   non_defected_file_count = len([x_ for x_ in all_labels if x_==0.0])
   print "No of. defects={}, non-defects={}".format(defected_file_count, non_defected_file_count)
   print "-"*50
   feature_names = getColumnNames(ds_file_name, [0, 1, feature_cols])
   print feature_names

   calcFeatureImp(all_features, all_labels)
