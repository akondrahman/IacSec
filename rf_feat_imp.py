'''
Akond Rahman
Nov 15, 2017
Wednesday
Feature importance for IaC Metrics using RF
'''



if __name__=='__main__':
   full_ds, col_names=readDataset(ds_file_name)
   calcFeatureImp(full_ds)
