'''
Akond Rahman
Feb 07, 2018
Script to extract time wise data extract
'''
import os
import shutil
import subprocess

def get_immediate_subdirs(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def generatePastData(folder_path, y_p, m_p):
    all_dirs = get_immediate_subdirs(folder_path)
    for dir_ in all_dirs:
        srcFolder = folder_path + dir_ + '/'
        for year_ in y_p:
            for mont_ in m_p:
                folder2create = folder_path + dir_ + '-' + year_ + '-' + mont_ + '/'
                print '='*50
                print folder2create
                print '-'*25
                if((os.path.exists(folder2create))==False):
                  try:
                      shutil.copytree(srcFolder, folder2create)
                      '''
                      now  do a reset
                      '''
                      cdCommand            = "cd " + folder2create + " ; "
                      date2reset           = year_ + '-' + mont_ + '-' + '28'  ## 28 th of the month
                      commitCommand        = "git checkout `git rev-list -n 1 --before='"+ date2reset +"' master`"
                      command2Run          = cdCommand + commitCommand
                      subprocess.check_output(['bash','-c', command2Run])
                  except shutil.Error as err_:
                      print 'Directory not copied, error:', err_
                print '='*50

if __name__=='__main__':
   # folder2walk = '/Users/akond/SECU_REPOS/test-pup/'
   # y_list = ['2011', '2012', '2013', '2014', '2015', '2016']
   # m_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']


   folder2walk = '/Users/akond/SECU_REPOS/wiki-pupp/'
   y_list = ['2011', '2012', '2013', '2014', '2015', '2016']
   m_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

   generatePastData(folder2walk, y_list, m_list)
