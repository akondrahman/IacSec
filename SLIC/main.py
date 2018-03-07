'''
Akond Rahman
Feb 08, 2018
This code executes the lint engine
'''
import executor
import time
import datetime

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

if __name__=='__main__':
   print 'Started at:', giveTimeStamp()
   print '*'*125
   ds_path = '/Users/akond/SECU_REPOS/test-pupp/'

   # ds_path = '/Users/akond/SECU_REPOS/test-chef/'

   executor.sniffSmells(ds_path)
   print '*'*125
   print 'Ended at:', giveTimeStamp()
