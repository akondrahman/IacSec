'''
Akond Rahman
Feb 08, 2018
This code executes the lint engine
'''
import executor
import time
import datetime
import constants
import os

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

if __name__=='__main__':
   t1 = time.time()
   print 'Started at:', giveTimeStamp()
   print '*'*100

   '''
   PUPPET DIRECTORIES
   '''
   # ds_path = '/Users/akond/SECU_REPOS/test-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/TEST_PUPPET.csv'

   # ds_path = '/Users/akond/SECU_REPOS/mozi-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_MOZILLA_PUPPET.csv'

   # ds_path = '/Users/akond/SECU_REPOS/ostk-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_OPENSTACK_PUPPET.csv'

   # ds_path = '/Users/akond/SECU_REPOS/wiki-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_WIKIMEDIA_PUPPET.csv'

   '''
   CHEF DIRECTORIES
   '''
   ds_path = '/Users/akond/SECU_REPOS/test-chef/'
   output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/TEST_CHEF.csv'

   # ds_path = '/Users/akond/SECU_REPOS/berg-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_BERG_CHEF.csv'

   # ds_path = '/Users/akond/SECU_REPOS/cdat-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_CDAT_CHEF.csv'

   # ds_path = '/Users/akond/SECU_REPOS/expr-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_EXPR_CHEF.csv'

   final_output_str, final_symbol_str = executor.sniffSmells(ds_path) # 1. count, 2. symbols for whcih we observe smells
   final_output_str = constants.HEADER_STR + '\n' +  final_output_str
   final_symbol_str = constants.SYM_HEAD + '\n' +  final_symbol_str
   print '*'*100
   print final_symbol_str
   bytes_out = dumpContentIntoFile(final_output_str, output_file)
   print 'Dumped output file of {} bytes'.format(bytes_out)
   print '*'*100
   print 'Ended at:', giveTimeStamp()
   print '*'*100
   t2 = time.time()
   diff = (t2 - t1 ) / 60
   print "Duration: {} minutes".format(diff)
   print '*'*100
