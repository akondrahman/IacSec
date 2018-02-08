'''
Akond Rahman
Feb 08, 2018
This code executes the lint engine
'''
import executor

if __name__=='__main__':
   ds_path = '/Users/akond/SECU_REPOS/test-pupp/'

   # ds_path = '/Users/akond/SECU_REPOS/test-chef/'

   executor.sniffSmells(ds_path)
