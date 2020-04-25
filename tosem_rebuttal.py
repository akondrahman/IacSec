'''
Akond Rahman 
Apr 23 2020 
Thursday 
TOSEM REBUTTAL
'''
from datetime import datetime
import numpy as np 
import pandas as pd 
import os 
import csv 
import time
import datetime
from git import Repo
import  subprocess
import math 
from collections import Counter

def getEligibleProjects(fileNameParam):
  repo_list = []
  with open(fileNameParam, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
      repo_list.append(row[0])
  return repo_list

def getPuppetFilesOfRepo(repo_dir_absolute_path, extension):
    print(repo_dir_absolute_path) 
    pp_, pp_non_pp = [], []
    for root_, dirs, files_ in os.walk(repo_dir_absolute_path):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           pp_non_pp.append(full_p_file)
           if((os.path.exists(full_p_file)) and ('EXTRA_AST' not in full_p_file) ):
             if (full_p_file.endswith(extension)):
                #  print(full_p_file) 
                 pp_.append(full_p_file)
    return  pp_non_pp,  pp_



def getRelPathOfFiles(all_pp_param, repo_dir_absolute_path):
  common_path = repo_dir_absolute_path
  files_relative_paths = [os.path.relpath(path, common_path) for path in all_pp_param]
  return files_relative_paths 

def getDevsOfRepo(repo_path_param):
   commit_dict       = {}
   author_dict       = {}

   cdCommand         = "cd " + repo_path_param + " ; "
   commitCountCmd    = " git log --pretty=format:'%H_%an' "
   command2Run = cdCommand + commitCountCmd

   commit_count_output = subprocess.check_output(['bash','-c', command2Run])
   commit_count_output = str(commit_count_output) 
   author_count_output = commit_count_output.split('\n')
   for commit_auth in author_count_output:
       commit_ = commit_auth.split('_')[0]
       
       author_ = commit_auth.split('_')[1]
       author_ = author_.replace(' ', '')
       # only one author for one commit 
       if commit_ not in commit_dict:
           commit_dict[commit_] = author_ 
       # one author can be involved with multiple commits 
       if author_ not in author_dict:
           author_dict[author_] = [commit_] 
       else:            
           author_dict[author_] = author_dict[author_] + [commit_] 
   return commit_dict, author_dict   


def getBranchName(proj_):
    branch_name = ''
    proj_branch = {'biemond@biemond-oradb':'puppet4_3_data', 'derekmolloy@exploringBB':'version2', 'exploringBB':'version2', 
                'jippi@puppet-php':'php7.0', 'maxchk@puppet-varnish':'develop', 'threetreeslight@my-boxen':'mine', 
                'puppet':'production'
              } 
    if proj_ in proj_branch:
        branch_name = proj_branch[proj_]
    else:
        branch_name = 'master'
    return branch_name

def getIaCRelatedCommits(repo_dir_absolute_path, ppListinRepo, ext_param , branchName='master'):
  mappedPuppetList=[]
  track_exec_cnt = 0
  repo_  = Repo(repo_dir_absolute_path)
  all_commits = list(repo_.iter_commits(branchName))
  for each_commit in all_commits:
    track_exec_cnt = track_exec_cnt + 1

    cmd_of_interrest1 = "cd " + repo_dir_absolute_path + " ; "
    # cmd_of_interrest2 = "git show --name-status " + str(each_commit)  +  "  | awk '/.pp/ {print $2}'" 
    cmd_of_interrest2 = "git show --name-status " + str(each_commit)  +  "  | awk '/" + ext_param + "/ {print $2}'" 
    cmd_of_interrest = cmd_of_interrest1 + cmd_of_interrest2
    commit_of_interest  = subprocess.check_output(['bash' , '-c', cmd_of_interrest])
    commit_of_interest = str(commit_of_interest)     

    for ppFile in ppListinRepo:
      if ppFile in commit_of_interest:

       file_with_path = os.path.join(repo_dir_absolute_path, ppFile)
       mapped_tuple = (file_with_path, each_commit)
       mappedPuppetList.append(mapped_tuple)

  return all_commits, mappedPuppetList

def getGitDevEmailsOfRepo(repo_path_param):
   per_repo_emails = []
   cdCommand         = "cd " + repo_path_param + " ; "
   commitCountCmd    = " git log --pretty=format:'%H_%aE' " # E for email, n for name 
   command2Run = cdCommand + commitCountCmd

   commit_count_output = subprocess.check_output(['bash','-c', command2Run])
   commit_count_output = commit_count_output.decode('utf-8')
   author_count_output = commit_count_output.split('\n')

   for commit_auth in author_count_output:
       commit_ = commit_auth.split('_')[0]       
       author_ = commit_auth.split('_')[1]
       author_ = author_.replace(' ', '')
       per_repo_emails.append(author_) 
   #print(per_repo_emails) 
   per_repo_emails = np.unique(per_repo_emails)  
   return per_repo_emails

def printStartDate(org_, proj_):
      print('*'*50)
      repo_path   = '/Users/arahman/PRIOR_NCSU/SECU_REPOS/' + org_ + "/" + proj_
      print(repo_path)
      repo_  = Repo(repo_path)
      all_commits = list(repo_.iter_commits('master'))  
      all_day_list = []   
      for commi_ in all_commits:
        timestamp_commit = commi_.committed_datetime
        str_time_commit  = timestamp_commit.strftime(  "%Y-%m-%dT%H-%M-%S" ) ## date with time   
        all_day_list.append( str_time_commit ) 

      all_day_list   = [x_.split('T')[0] for x_ in all_day_list]
      all_day_list   = np.unique( all_day_list )
      # print(all_day_list) 
      all_day_list   = [ datetime.datetime(int(x_.split('-')[0]), int(x_.split('-')[1]), int(x_.split('-')[2]), 12, 30) for x_ in all_day_list]
      min_day        = min(all_day_list) 
      print(min_day)
      print('*'*50)      


def getNeededMetrics(orgParamName, repo_name_param, branchParam , extParam ):
    dict2ret = {} 
    repo_path   = '/Users/arahman/PRIOR_NCSU/SECU_REPOS/' + orgParamName + "/" + repo_name_param
    # print(repo_path)
    repo_branch = getBranchName(repo_name_param)    
    all_devs_in_repo = getGitDevEmailsOfRepo( repo_path ) 
    all_files_in_repo, all_pp_files_in_repo = getPuppetFilesOfRepo(repo_path, extParam)   
    rel_path_pp_files = getRelPathOfFiles(all_pp_files_in_repo, repo_path)
    all_commits_in_repo, pupp_commits_in_repo = getIaCRelatedCommits(repo_path, rel_path_pp_files, extParam, repo_branch)
    all_devs_in_repo = np.unique(all_devs_in_repo)  
    # print(all_devs_in_repo) 
    iac_fil_siz = 0 
    for x_ in all_pp_files_in_repo:
      iac_fil_siz = iac_fil_siz + sum(1 for line_ in x_) 
    dict2ret = {'REPO':repo_path,  'DEVS':len(all_devs_in_repo), 'ALL_COMMITS':len(all_commits_in_repo), 
                            'IAC_COMMITS':len(pupp_commits_in_repo), 'ALL_FILES':len(all_files_in_repo), 
                            'ALL_IAC_FILES':len(all_pp_files_in_repo), 'ALL_IAC_SIZE': iac_fil_siz  
    }

    return dict2ret

if __name__=='__main__':
  # orgName = 'ostk-chef'
  # extName = '.rb'

  orgName = 'ostk-ansi'
  extName = '.yaml'

  tot_dev, tot_com, tot_iac_com, tot_fil, tot_iac_fil, tot_iac_siz  = 0, 0, 0, 0, 0, 0
  fileName          = '/Users/arahman/PRIOR_NCSU/SECU_REPOS/'  + orgName + '/' + 'eligible_repos.csv' 
  elgibleRepos      = getEligibleProjects(fileName)
  for proj_ in elgibleRepos:
      metrics_as_dict = getNeededMetrics( orgName, proj_,  'master', extName ) 
      tot_dev         = tot_dev + metrics_as_dict['DEVS'] 
      tot_com         = tot_com + metrics_as_dict['ALL_COMMITS'] 
      tot_iac_com     = tot_iac_com + metrics_as_dict['IAC_COMMITS'] 
      tot_fil         = tot_fil + metrics_as_dict['ALL_FILES']
      tot_iac_fil     = tot_iac_fil + metrics_as_dict['ALL_IAC_FILES']
      tot_iac_siz     = tot_iac_siz + metrics_as_dict['ALL_IAC_SIZE']
      printStartDate(orgName, proj_) 
  print('ORG_NAME, REPO_CNT, DEV_CNT, COMMIT_CNT, IAC_COMM_CNT, IAC_FILE_CNT, IAC_FIL_SIZ')
  print( orgName, len(elgibleRepos), tot_dev, tot_com, tot_iac_com, tot_iac_fil, tot_iac_siz)  

  '''
  ORG_NAME, REPO_CNT, DEV_CNT, COMMIT_CNT, IAC_COMM_CNT, IAC_FILE_CNT, IAC_FIL_SIZ
  ostk-chef 11           650         4758       8967     1129             124808
  ostk-ansi 16          1175        20294       2266     1120             138679
  '''

  '''
  
  '''