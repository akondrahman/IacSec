'''
Akond Rahman
Author metrics extractor from git repositories
Mar 08 2019
'''

import os, subprocess, numpy as np, operator
from  collections import Counter
from  scipy.stats import entropy
import pandas as pd 
from collections import Counter

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)


def getUniqueDevCount(param_file_path, repo_path):

   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   commitCountCmd    = " git blame "+ theFile +"  | awk '{print $2}' | cut -d'(' -f2 "
   command2Run = cdCommand + commitCountCmd

   commit_count_output = subprocess.check_output(['bash','-c', command2Run])
   author_count_output = commit_count_output.split('\n')
   author_count_output = [x_ for x_ in author_count_output if x_!='']
   author_count        = len(np.unique(author_count_output))

   return author_count


def getMinorContribCount(param_file_path, repo_path, sloc):
   minorList = []
   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   blameCommand      = " git blame " + theFile + "  | awk '{print $2}'  | cut -d'(' -f2"
   command2Run       = cdCommand + blameCommand

   blame_output   = subprocess.check_output(['bash','-c', command2Run])
   blame_output   = blame_output.split('\n')
   blame_output   = [x_ for x_ in blame_output if x_!='']
   author_contrib = dict(Counter(blame_output))

   for author, contribs in author_contrib.items():
      if((float(contribs)/float(sloc)) < 0.05):
        minorList.append(author)
   return len(minorList)

def getMajorContribCount(param_file_path, repo_path, sloc):
   majorList = []
   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   blameCommand      = " git blame " + theFile + "  | awk '{print $2}'  | cut -d'(' -f2"
   command2Run       = cdCommand + blameCommand

   blame_output      = subprocess.check_output(['bash','-c', command2Run])
   blame_output      = blame_output.split('\n')
   blame_output      = [x_ for x_ in blame_output if x_!='']
   author_contrib    = dict(Counter(blame_output))

   for author, contribs in author_contrib.items():
      if((float(contribs)/float(sloc)) >= 0.05):
        majorList.append(author)
   return len(majorList)


def getHighestContribsPerc(param_file_path, repo_path, sloc):
   owner_contrib = 0 
   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(param_file_path, repo_path)
   blameCommand      = " git blame " + theFile + "  | awk '{print $2}'  | cut -d'(' -f2"
   command2Run       = cdCommand + blameCommand

   blame_output     = subprocess.check_output(['bash','-c', command2Run])
   blame_output     = blame_output.split('\n')
   blame_output     = [x_ for x_ in blame_output if x_!='']
   author_contrib   = dict(Counter(blame_output))

   if (len(author_contrib) > 0):
     highest_author   = max(author_contrib.iteritems(), key=operator.itemgetter(1))[0]
     highest_contr    = author_contrib[highest_author]
   else:
     highest_contr = 0
   if sloc <= 0 :
       sloc += 1
   owner_contrib = (round(float(highest_contr)/float(sloc), 5))
   return owner_contrib


def getRecentExp(file_path, repo_path):
   per_author_dict   = {}
   final_recent_exp_dict = {}
   cdCommand         = "cd " + repo_path + " ; "
   theFile           = os.path.relpath(file_path, repo_path)
   blameCommand      = " git blame -e " + theFile + " | awk '{print $2\"_\"$3\"T\"$4}' | cut -d'(' -f2" ## awk can pritn stuff with "", to specify ", use \"
   command2Run       = cdCommand + blameCommand

   blame_output      = subprocess.check_output(['bash','-c', command2Run])
   blame_output      = blame_output.split('\n')
   blame_output      = [x_ for x_ in blame_output if x_!='']

   # print blame_output
   # uni_authors       = np.unique([x_.split('@')[0] for x_ in blame_output])
   # print blame_output 
   # print uni_authors 
   for per_author_blame in blame_output:
       per_author_email = per_author_blame.split('@')[0]
       per_author_date  = per_author_blame.split('T')[1]        
       per_author_year  = per_author_date.split('-')[0]
       if '200' not in per_author_year:
           per_author_year = '2019'
       if per_author_email not in per_author_dict:
              per_author_dict[per_author_email] = [per_author_year]  
       else: 
              per_author_dict[per_author_email] = per_author_dict[per_author_email] + [per_author_year]  
   # print per_author_dict
   for k_, v_ in per_author_dict.iteritems():
       year_list = [int(x_) for x_ in v_ ]
       dict_ = dict(Counter(year_list)) 
       total_lines = len(year_list) 
       unique_years = list(np.unique(year_list)) 
       unique_years.sort(reverse = True) 
       recent_exp_list = []
       for year_index in xrange(len(unique_years)):
           year_ = unique_years[year_index] 
           contribs = dict_[year_] 
           recent_exp = float(contribs) / float(year_index + 1)
           recent_exp_list.append(recent_exp) 
       recent_exp_final = sum(recent_exp_list) 
       #  print k_, recent_exp_final 
       final_recent_exp_dict[k_] = recent_exp_final 
   print final_recent_exp_dict 
   return final_recent_exp_dict

       


def getProcessMetrics(file_path_p, repo_path_p):
    LOC          = sum(1 for line in open(file_path_p))

    DEV          = getUniqueDevCount(file_path_p, repo_path_p)
    MINOR        = getMinorContribCount(file_path_p, repo_path_p, LOC)
    MAJOR        = getMajorContribCount(file_path_p, repo_path_p, LOC)
    OWNER_LINES  = getHighestContribsPerc(file_path_p, repo_path_p, LOC)
    RECENT_EXP   = getRecentExp(file_path_p, repo_path_p) ## computed but not used 

    all_process_metrics = str(DEV) + ',' + str(MINOR) + ',' + str(MAJOR) + ',' + str(OWNER_LINES) 

    return all_process_metrics, DEV

if __name__=='__main__':
    SLIC_OUTPUT_FILE   = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_TEST_CHEF.csv'
    AUTHOR_OUTPUT_FILE = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_TEST_AUHTOR_CHEF.csv'

    final_str = ''
    SLIC_OUT_DF = pd.read_csv(SLIC_OUTPUT_FILE) 
    all_files   = np.unique( SLIC_OUT_DF['FILE_NAME'].tolist() )
    for file_ in all_files:
        print 'Processing:', file_ 
        repo_dir_  = SLIC_OUT_DF[SLIC_OUT_DF['FILE_NAME']==file_]['REPO_DIR'].tolist()[0]
        repo_dir_  = repo_dir_ + '/'
        #print repo_dir_ 
        SMELL_CNT  = SLIC_OUT_DF[SLIC_OUT_DF['FILE_NAME']==file_]['TOTAL'].tolist()[0]
        if SMELL_CNT > 0:
           SMELL_FLAG = 1 
        else:
           SMELL_FLAG = 0 

        author_metrics, devCount = getProcessMetrics(file_, repo_dir_)

        if devCount > 0 :
           per_file_str = repo_dir_ + ',' + file_ + ',' + author_metrics + ',' + str(SMELL_CNT) + ',' + str(SMELL_FLAG) 
        final_str = final_str + per_file_str + '\n' 
    
    final_str = 'REPO,FILE,DEV,MINOR,MAJOR,OWNER_LINES,SMELL_COUNT,SMELL_FLAG' + '\n' + final_str 
    dumpContentIntoFile(final_str, AUTHOR_OUTPUT_FILE)
