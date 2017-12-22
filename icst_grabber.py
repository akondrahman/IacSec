'''
Akond Rahman
Dec 22, 2017
Friday
Code to extract data for ICST paper
'''
import csv
import os
import numpy as np
import cPickle as pickle
def getContent(list_of_ds):
    counter = 0
    dictOfAllFiles, dict2Ret = {}, {}
    for ds_ in list_of_ds:
            print 'Processing:', ds_
            print '-'*100
            with open(ds_, 'rU') as file_:
              reader_ = csv.reader(file_)
              next(reader_, None)
              for row_ in reader_:
                repo_of_file       = row_[1]
                categ_of_file      = row_[3]
                full_path_of_file  = row_[4]
                if os.path.exists(full_path_of_file):
                   if full_path_of_file not in dictOfAllFiles:
                      dictOfAllFiles[full_path_of_file] = [ categ_of_file ]
                   else:
                      dictOfAllFiles[full_path_of_file] = dictOfAllFiles[full_path_of_file] + [ categ_of_file ]
    print 'Total valid scripts:', len(dictOfAllFiles)
    print '-'*100
    for k_, v_ in dictOfAllFiles.items():
               counter += 1
               uniq = np.unique(v_)
               with open(k_, 'rU') as the_file:
                    the_content = the_file.read()
               if ((len(uniq)==1) and (uniq[0]=='N')):
                 dict2Ret[counter] = (the_content, '0')
               else:
                 dict2Ret[counter] = (the_content, '1')
    return dict2Ret





if __name__=='__main__':
   moz='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Mozilla.Final.Categ.csv'
   ost='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Openstack.WithoutBadBoys.Final.Categ.csv'
   wik='/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Wikimedia.Final.Categ.csv'
   ds_list = [moz, ost, wik]
   all_file_dump=getContent(ds_list)
   pickle.dump( all_file_dump, open( "SCRIPT.LABELS.DUMP", "wb" ) )
   all_script_dict = pickle.load( open('SCRIPT.LABELS.DUMP', 'rb'))
   # print all_script_dict   
