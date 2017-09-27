'''
Akond Rahman
Sep 27, 2017
to get lanuchpad's description reports' text
and check for secuirty key words
'''
from launchpadlib.launchpad import Launchpad
import numpy as np
import utility
cachedir  = '/Users/akond/.launchpadmat/'
launchpad = Launchpad.login_anonymously('LPAD_DESC_DLOAD', 'production', cachedir, version='devel')
launchpad_file_name = 'ost.lpad.ids.txt'
sec_kw_file_name    = 'sec.kws.txt'
not_exist_list = [1]
counter = 0


if __name__=='__main__':
   bugID2Dump = []
   bugMSG2Dump = []
   with open(launchpad_file_name) as f:
        content = f.readlines()
   with open(sec_kw_file_name) as f_:
        sec_kw_content = f_.readlines()
   sec_kw_content = [sec_kw.strip() for sec_kw in sec_kw_content]
   sec_kw_content = [sec_kw.lower() for sec_kw in sec_kw_content]

   lpad_ids = [x.strip() for x in content]
   lpad_ids = np.unique(lpad_ids)
   lpad_ids = [int(lpad_id) for lpad_id in lpad_ids]
   lpad_ids = [lpad_id for lpad_id in lpad_ids if lpad_id not in not_exist_list]
   valid_lpad_cnt = len(lpad_ids)
   print 'before filtering:{}, after filtering:{}'.format(len(content), valid_lpad_cnt)
   match_cnt = 0
   for lpad_id in lpad_ids:
       counter += 1
       matching_sec_kw = 'LOL'
       sec_flag = False
       try:
          the_lpad    =  launchpad.bugs[lpad_id]
          lpad_mesg   =  the_lpad.description
          for sec_kw in sec_kw_content:
              if(sec_kw in lpad_mesg):
                      sec_flag = True
                      matching_sec_kw=sec_kw
                      bugMSG2Dump.append(lpad_mesg)
          if (sec_flag):
                 match_cnt += 1
                 print 'FOUND STH!!!'
                 print 'BUGID:{},MATCHING-KW:{},MATCH-CNT:{}'.format(lpad_id, matching_sec_kw, match_cnt)
                 bugID2Dump.append(lpad_id)
                 print '*'*25
          print '='*50
          print "Processed {} bug IDs, {} left".format(counter, valid_lpad_cnt - counter)
          print '='*50
       except Exception as e:
          print 'Caught exception:', e.message
   '''
   DUMP LIST AS STR
   '''
   str2write = ''
   for id_ in bugID2Dump:
       str2write = str2write + str(id_) + ',' + '\n'

   utility.dumpContentIntoFile(str2write, '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/REPORTIDS_WITH_SEC_OST.csv')
   '''
   DUMP REPORTS AS STR
   '''
   report_no = 0 
   for report_ in bugMSG2Dump:
       report_no += 1
       tokens = report_.split(' ')
       report_ = ''
       for token_ in tokens:
         try:
            token_ = token_.encode('ascii', 'ignore').decode('ascii')
            token_ = token_.strip()
            token_ = token_.lower()
         except TypeError:
            token_ = token_.lower()
            token_ = token_.strip()
         report_ = report_ + token_ + ' '
       file2save = str(report_no) + '_BURN_AFTER_READING.txt'
       utility.dumpContentIntoFile(report_, '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/OST/' + file2save)
       report_ = ''
