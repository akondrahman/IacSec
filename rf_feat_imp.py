'''
Akond Rahman
Nov 15, 2017
Wednesday
Feature importance for IaC Metrics using RF
'''
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

def readDataset(fileParam, dataTypeFlag=True):
  if dataTypeFlag:
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')
  return data_set_to_return

def getColumnNames(file_name_param, start, end ):
    ds_   = pd.read_csv(file_name_param)
    temp_ = list(ds_.columns.values)
    temp_ = temp_[start:end]
    return temp_

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

def calcFeatureImp(feature_vec, label_vec, feature_names_param, output_file, repeat=10):
    header_str, str2write= '', ''
    for name_ in feature_names_param:
        header_str = header_str + name_ + ','
    theRndForestModel = RandomForestClassifier()
    theRndForestModel.fit(feature_vec, label_vec)
    feat_imp_vector=theRndForestModel.feature_importances_
    #print feat_imp_vector

    for ind_ in xrange(repeat):
        for imp_vec_index in xrange(len(feat_imp_vector)):
            feat_imp_val = round(feat_imp_vector[imp_vec_index], 5)
            str2write = str2write +  str(feat_imp_val) + ','
            # print 'Anti-pattern:{}, score:{}'.format(feature_names_param[imp_vec_index], feat_imp_val)
            # print '-'*25
        str2write = str2write + '\n'
    str2write = header_str + '\n' + str2write
    output_status= dumpContentIntoFile(str2write, output_file)
    print 'Dumped the RF FEATURE IMPORTANCE file of {} bytes'.format(output_status)

def calcRFE(feature_vec, label_vec, feature_names_param):
    # http://blog.datadive.net/selecting-good-features-part-iv-stability-selection-rfe-and-everything-side-by-side/

    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import MultinomialNB

    lr_estimator = LogisticRegression()
    nb_estimator = MultinomialNB()
    for estimator in (lr_estimator, nb_estimator):
            selector  = RFE(estimator, 5, step=1)
            selector  = selector.fit(feature_vec, label_vec)
            elim_deci = selector.support_
            all_ranks = selector.ranking_ # 1 means highest rank
            for feature, deci in zip(feature_names_param, elim_deci):
                print "METRIC:{},DECISION:{}".format(feature, deci)
            print '*'*25
            for feature, rank in zip(feature_names_param, all_ranks):
                print "METRIC:{},RANK:{}".format(feature, rank)
            print '='*50

if __name__=='__main__':
   # ds_file_name       = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_BASTION_FULL_PROCESS_DATASET.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/BASTION.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/NO-COMM-AGE/CIS.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/CISCO.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/NO-COMM-AGE/MIR.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/MIRANTIS.csv'

   # ds_file_name       = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/reproc/DEFECT-Datasets/MOZILLA_DEFECT_DATASET.csv"
   # ds_file_name       = "/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/NO-COMM-AGE/MOZ.csv"
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/MOZILLA.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/emse/FI_MOZILLA.csv'

   # ds_file_name       = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/reproc/DEFECT-Datasets/OPENSTACK_DEFECT_DATASET.csv"
   # ds_file_name="/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/NO-COMM-AGE/OST.csv"
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/OPENSTACK.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/emse/FI_OPENSTACK.csv'

   # ds_file_name       = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/reproc/DEFECT-Datasets/WIKIMEDIA_DEFECT_DATASET.csv"
   # ds_file_name="/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/NO-COMM-AGE/WIK.csv"
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/WIKIMEDIA.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Prediction-Project/results/emse/FI_WIKIMEDIA.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_MIRANTIS_FULL_DATASET.csv'
   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_MOZ_FULL_DATASET.csv'
   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_OST_FULL_DATASET.csv'
   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_WIKI_FULL_DATASET.csv'

   '''
   ICSE 19 / FSE 19 PUSH
   '''
   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/ICSE19_TSE/MIR_FUL_PRO.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/ICSE19_TSE/MIR.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/ICSE19_TSE/MOZ_FUL_PRO.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/ICSE19_TSE/MOZ.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/ICSE19_TSE/OST_FUL_PRO.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/ICSE19_TSE/OST.csv'

   # ds_file_name='/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/ICSE19_TSE/WIK_FUL_PRO.csv'
   # output_file_param  = '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/output/rf_feat_imp/ICSE19_TSE/WIK.csv'

   full_ds=readDataset(ds_file_name)
   full_rows, full_cols = np.shape(full_ds)
   feature_cols = full_cols - 1
   all_features = full_ds[:, 2:feature_cols]
   all_labels  =  full_ds[:, feature_cols]
   defected_file_count     = len([x_ for x_ in all_labels if x_==1.0])
   non_defected_file_count = len([x_ for x_ in all_labels if x_==0.0])
   feature_names = getColumnNames(ds_file_name, 2, feature_cols)
   calcFeatureImp(all_features, all_labels, feature_names, output_file_param)
   print '='*100
   print ds_file_name
   # calcRFE(all_features, all_labels, feature_names)
   print '='*100
