'''
Akond Rahman 
June 27, 2018 
Download repos from Github 
'''
import os 
import csv 
import subprocess
import numpy as np

def getRepos(file_name):
    list_ = []
    with open(file_name, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
          the_repo_name = row_[0]
          repo_dload_url = 'https://github.com/' + the_repo_name + '.git'
          list_.append(repo_dload_url)
          #https://github.com/akondrahman/SolidityExploration.git    
    return list_


if __name__=='__main__':
   srcFile1='/Users/akond.rahman/Documents/Personal/misc/icse19-work/gh-repo-list-batch1.csv'
   srcFile2='/Users/akond.rahman/Documents/Personal/misc/icse19-work/gh-repo-list-batch2.csv'
   list1=getRepos(srcFile1)    
   list2=getRepos(srcFile2)      
   list = list1 + list2 
   list_ = np.unique(list)
   print 'Repos to download:', len(list_)