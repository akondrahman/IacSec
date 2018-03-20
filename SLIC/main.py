'''
Akond Rahman
Feb 08, 2018
This code executes the lint engine
'''
import cPickle as pickle
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

def dumpContentIntoPickle(listP, fileP):
    with open(fileP, 'wb') as f_:
         pickle.dump(listP, f_)
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
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_TEST_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_TEST_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/mozi-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_MOZILLA_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_ALL_MOZ_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/ostk-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_OPENSTACK_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_ALL_OST_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/wiki-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_WIKIMEDIA_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_ALL_WIK_PUP.PKL'

   '''
   CHEF DIRECTORIES
   '''
   # ds_path = '/Users/akond/SECU_REPOS/test-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_TEST_CHEF.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_TEST.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/berg-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_BERG_CHEF.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_BERG.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/cdat-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_CDAT_CHEF.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_CDAT.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/expr-chef/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_ALL_EXPR_CHEF.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V4_SYM_CHEF.PKL'

   final_output_str, sym_out_full = executor.sniffSmells(ds_path) # 1. count, 2. symbols for whcih we observe smells
   final_output_str = constants.HEADER_STR + '\n' +  final_output_str
   print '*'*100
   # print sym_out_full
   bytes_out = dumpContentIntoFile(final_output_str, output_file)
   print 'Dumped output file of {} bytes'.format(bytes_out)
   print '*'*100
   sym_out = dumpContentIntoPickle(sym_out_full, sym_output_file)
   print 'Dumped symbolic output PICKLE of {} bytes'.format(sym_out)
   print '*'*100
   print 'Ended at:', giveTimeStamp()
   print '*'*100
   t2 = time.time()
   diff = (t2 - t1 ) / 60
   print "Duration: {} minutes".format(diff)
   print '*'*100
