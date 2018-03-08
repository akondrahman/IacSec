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
   # ds_path = '/Users/akond/SECU_REPOS/test-pupp/'
   # output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_PUPPET.csv'

   ds_path = '/Users/akond/SECU_REPOS/test-chef/'
   output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/ALL_CHEF.csv'

   final_output_str = executor.sniffSmells(ds_path)
   final_output_str = constants.HEADER_STR + '\n' +  final_output_str
   print '*'*100
   # print final_output_str
   bytes_out = dumpContentIntoFile(final_output_str, output_file)
   print 'Dumped output file of {} bytes'.format(bytes_out)
   print '*'*100
   print 'Ended at:', giveTimeStamp()
   print '*'*100
   t2 = time.time()
   diff = t2 - t1
   print "Duration: {} seconds".format(diff)
   print '*'*100
