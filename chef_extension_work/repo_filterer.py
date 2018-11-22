'''
Collect Chef scripts from Openstack 
Akond Rahman 
Nov 21, 2018 
'''
import subprocess
import os 
from datetime import datetime
import numpy as np 

def getFileLines(file_para):
    file_lines = []
    with open(file_para, 'rU') as log_fil:
         file_str = log_fil.read()
         file_lines = file_str.split('\n')
    file_lines = [x_ for x_ in file_lines if x_ != '\n']
    return file_lines

def getCount(dir_name):
    chef_, non_chef = [], []
    for root_, dirs, files_ in os.walk(dir_name):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if(os.path.exists(full_p_file)):
             if ( 'cookbook' in full_p_file) and (full_p_file.endswith('.rb')):
               chef_.append(full_p_file)
             else:
               non_chef.append(full_p_file)    

    tot = len(chef_) + len(non_chef) 
    return tot, len(chef_)

def getCommitCount(repo_path):
   totalCountForChurn = 0

   cdCommand     = "cd " + repo_path + " ; "
   commitCount   = "git log --pretty=oneline ; "
   command2Run   = cdCommand + commitCount

   dt_churn_output = subprocess.check_output(['bash','-c', command2Run])
   dt_churn_output = dt_churn_output.split('\n')
   dt_churn_output = [x_ for x_ in dt_churn_output if x_!='']
   totalCountForChurn = len(dt_churn_output)
   return totalCountForChurn

def getUniqueDevCount( repo_path):

   cdCommand         = "cd " + repo_path + " ; "

   commitCountCmd    = " git log --pretty=format:'%h%x09%an'  | awk '{ print $2 $3 }' "
   command2Run = cdCommand + commitCountCmd

   commit_count_output = subprocess.check_output(['bash','-c', command2Run])
   author_count_output = commit_count_output.split('\n')
   author_count_output = [x_ for x_ in author_count_output if x_!='']
   author_count        = len(np.unique(author_count_output))
   return author_count


def getMonthDiff(repo_path):
   cdCommand        = "cd " + repo_path + " ; "
   lastCommitCmd    = " git log -1 --date=short --pretty=format:%cd "
   lastCmd2Run      = cdCommand + lastCommitCmd
   last_commit_date = subprocess.check_output(['bash','-c', lastCmd2Run])


   firstCommitCmd    = "alu=`git log --pretty=format:%H | tail -1`; git log -1 --date=short --pretty=format:%cd $alu ;"
   firstCmd2Run      = cdCommand + firstCommitCmd
   first_commit_date = subprocess.check_output(['bash','-c', firstCmd2Run])

   return last_commit_date, first_commit_date

def calculateMonthDiffFromTwoDates(early, latest):
    from datetime import datetime
    early_year   = early.split('-')[0]
    latest_year  = latest.split('-')[0]
    early_month  = early.split('-')[1]
    latest_month = latest.split('-')[1]
    early_dt     = datetime(int(early_year), int(early_month), 1)
    latest_dt    = datetime(int(latest_year), int(latest_month), 1)

    return (latest_dt.year - early_dt.year)*12 + latest_dt.month - early_dt.month

def getRepoFilterStats(dir_par):
    repo_file = dir_par + 'all.openstack.repos.txt'
    repo_dirs = getFileLines(repo_file)
    for repo_ in repo_dirs:
        repo_ = repo_.replace(' ', '')
        full_dir_p = dir_par + repo_ + '/'
        #print full_dir_p
        if (os.path.exists(full_dir_p)):
            tot_cnt, che_cnt = getCount(full_dir_p)  
            chef_perc = float(che_cnt) / float(tot_cnt)      
            commCount = getCommitCount(full_dir_p)
            devCount  = getUniqueDevCount(full_dir_p)
            last_comm_date, firs_comm_date = getMonthDiff(full_dir_p)
            #print last_comm_date, firs_comm_date
            monDiffCount = calculateMonthDiffFromTwoDates(firs_comm_date, last_comm_date)
            if monDiffCount == 0: 
                monDiffCount =  1
            comm_per_mon = float(commCount) / float(monDiffCount)

            print'{},{},{},{}'.format(repo_, chef_perc, comm_per_mon, devCount)


if __name__=='__main__':
   the_dir = '/Users/akond/SECU_REPOS/ostk-chef/'
   getRepoFilterStats(the_dir)