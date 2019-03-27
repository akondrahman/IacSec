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
   # ds_path =    '/Users/akond/SECU_REPOS/curated/agreed/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_CURATED_AGREE_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_CURATED_AGREE_PUP.PKL'

   # ds_path =    '/Users/akond/SECU_REPOS/curated/disagreed/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_CURATED_DISAGREE_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_CURATED_DISAGREE_PUP.PKL'

  #  ds_path = '/Users/akond/SECU_REPOS/test-pupp/'
  #  output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_TEST_PUPPET.csv'
  #  sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_TEST_PUP.PKL'

   ### CCS Rebuttal code
   # ds_path = '/Users/akond.rahman/Documents/Personal/misc/ccs-rebuttal-work/test/'
   # output_file = '/Users/akond.rahman/Documents/Personal/misc/ccs-rebuttal-work/CCS_REBUTTAL_TEST.csv'
   # sym_output_file = '/Users/akond.rahman/Documents/Personal/misc/ccs-rebuttal-work/CCS_REBUTTAL_TEST.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/mozi-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_MOZILLA_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_MOZ_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/ostk-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_OPENSTACK_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_OST_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/wiki-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_WIKIMEDIA_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_WIK_PUP.PKL'

   # ds_path = '/Users/akond/SECU_REPOS/ghub-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_GITHUB_PUPPET.csv'
   # sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_GIT_PUP.PKL'

   '''
   CHEF DIRECTORIES
   '''
   ds_path = '/Users/akond/SECU_REPOS/test-chef/'
   output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_TEST_CHEF.csv'
   sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_SYM_TEST_SLAC_CHEF.PKL'

  #  ds_path = '/Users/akond/SECU_REPOS/ostk-chef/'
  #  output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_OSTK_CHEF.csv'
  #  sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_SYM_OSTK_CHEF.PKL'

  #  ds_path = '/Users/akond/SECU_REPOS/ghub-chef/'
  #  output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_GHUB_CHEF.csv'
  #  sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_SYM_GHUB_SLIC_CHEF.PKL'

   final_output_str, sym_out_full = executor.sniffSmells(ds_path) # 1. count, 2. symbols for which we observe smells
   final_output_str = constants.HEADER_STR + '\n' +  final_output_str   ### header is used here
   print '*'*100
   # print sym_out_full
   bytes_out = dumpContentIntoFile(final_output_str, output_file)
   print 'Dumped CSV output file of {} bytes'.format(bytes_out)
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
