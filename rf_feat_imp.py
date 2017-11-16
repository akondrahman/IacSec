'''
Akond Rahman
Nov 15, 2017
Wednesday
Feature importance for IaC Metrics using RF
'''

def readDataset(fileParam, dataTypeFlag=True):
  if dataTypeFlag:
    data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1, dtype='float')
  else:
        data_set_to_return = np.genfromtxt(fileParam, delimiter=',', skip_header=1,  dtype='str')
  return data_set_to_return

def calcFeatureImp(feature_vec, label_vec):
    theRndForestModel = RandomForestClassifier()    

if __name__=='__main__':
   full_ds, col_names=readDataset(ds_file_name)
   full_rows, full_cols = np.shape(full_dataset_from_csv)
   feature_cols = full_cols - 1
   all_features = full_dataset_from_csv[:, 2:feature_cols]
   all_labels  =  dataset_for_labels[:, feature_cols]
   defected_file_count     = len([x_ for x_ in all_labels if x_==1.0])
   non_defected_file_count = len([x_ for x_ in all_labels if x_==0.0])
   print "No of. defects={}, non-defects={}".format(defected_file_count, non_defected_file_count)
   print "-"*50
   calcFeatureImp(full_ds)
