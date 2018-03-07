'''
Akond Rahman
Feb 08, 2018
This code executes the lint engine
'''
import executor
import time
import datetime
import constants

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

if __name__=='__main__':
   print 'Started at:', giveTimeStamp()
   print '*'*100
   # ds_path = '/Users/akond/SECU_REPOS/test-pupp/'

   ds_path = '/Users/akond/SECU_REPOS/test-chef/'

   final_output_str = executor.sniffSmells(ds_path)
   final_output_str = constants.HEADER_STR + '\n' +  final_output_str 
   print '*'*100
   print final_output_str
   print '*'*100
   print 'Ended at:', giveTimeStamp()
