'''
Akond Rahman
Author metrics extractor from git repositories
Mar 08 2019
'''

import os, subprocess, numpy as np, operator
from  collections import Counter
from  scipy.stats import entropy
import pandas as pd 

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



def getProcessMetrics(file_path_p, repo_path_p):
    LOC          = sum(1 for line in open(file_path_p))

    DEV          = getUniqueDevCount(file_path_p, repo_path_p)
    MINOR        = getMinorContribCount(file_path_p, repo_path_p, LOC)
    OWNER_LINES  = getHighestContribsPerc(file_path_p, repo_path_p, LOC)

    all_process_metrics = str(DEV) + ',' + str(MINOR) + ',' + str(OWNER_LINES) + ',' 

    return all_process_metrics

if __name__=='__main__':
    SLIC_OUTPUT_FILE= '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_SLIC_CHEF.csv'
    AUTHOR_OUTPUT_FILE = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_AUTHOR_CHEF.csv'

    final_str = ''
    SLIC_OUT_DF = pd.read_csv(SLIC_OUTPUT_FILE) 
    all_files   = np.unique( SLIC_OUT_DF['FILE_NAME'].tolist() )
    for file_ in all_files:
        repo_dir_  = SLIC_OUT_DF[SLIC_OUT_DF['FILE_NAME']==file_]['REPO_DIR'][0]
        SMELL_CNT  = SLIC_OUT_DF[SLIC_OUT_DF['FILE_NAME']==file_]['TOTAL'][0]
        if SMELL_CNT > 0:
           SMELL_FLAG = 1 
        else:
           SMELL_FLAG = 0 

        author_metrics = getProcessMetrics(file_, repo_dir_)
        per_file_str = repo_dir_ + ',' + file_ + ',' + author_metrics + ',' + str(SMELL_CNT) + ',' + str(SMELL_FLAG) 
        final_str = final_str + per_file_str + '\n' 
    
    dumpContentIntoFile(final_str, AUTHOR_OUTPUT_FILE)
