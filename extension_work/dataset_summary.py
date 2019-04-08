'''
Akond Rahman 
Mar 26, 2019 
Get dataset summary 
'''
import pandas as pd 
import numpy as np 
import os

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def getAllFiles(_dir):
    all_files = [] 
    for root_, dirs, files_ in os.walk(_dir):
       for file_ in files_:
        full_p_file = os.path.join(root_, file_)
        all_files.append(full_p_file)
    return all_files

def getAnsibleDetails(_dir):
    all_files, iac_files = [] , []
    for root_, dirs, files_ in os.walk(_dir):
       for file_ in files_:
        full_p_file = os.path.join(root_, file_)
        all_files.append(full_p_file)

    for root_, dirs, files_ in os.walk(_dir):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if('playbook' in full_p_file) and (full_p_file.endswith('.yml')):
               iac_files.append(full_p_file)

    return all_files, iac_files

def getSummary(df_pa, root_dir_):
    print 'Total repos:', len(get_immediate_subdirectories(root_dir_))
    print '-'*50
    file_list = np.unique(df_pa['FILE_NAME'].tolist())    
    print 'Total files:', len(getAllFiles(root_dir_))
    print '-'*50    
    print 'Total IaC files:', len(file_list)
    print '-'*50    
    sloc_list = [ sum(1 for line in open(x_, 'rU'))  for x_ in file_list]
    print 'Total SLOC:', sum(sloc_list) 
    print '-'*50        

if __name__=='__main__': 
    # root_dir = '/Users/akond/SECU_REPOS/ghub-chef/'
    # slac_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_GHUB_CHEF.csv'
    
    # root_dir = '/Users/akond/SECU_REPOS/ostk-chef/'
    # slac_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_OSTK_CHEF.csv'

    # root_dir = '/Users/akond/SECU_REPOS/ostk-ansi/'
    print root_dir
    print '-'*50 
    # df_ = pd.read_csv(slac_output_file) 
    # getSummary(df_, root_dir)


    # all_, iac_ = getAnsibleDetails(root_dir)    
    # print 'Total files:', len( all_ )
    # print '-'*50    
    # print 'Total IaC files:', len( iac_ )
    # print '-'*50        
    # sloc_list = [ sum(1 for line in open(x_, 'rU'))  for x_ in iac_]
    # print 'Total SLOC:', sum(sloc_list) 
    # print '-'*50        