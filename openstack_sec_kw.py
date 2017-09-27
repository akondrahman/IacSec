'''
Akond Rahman
Sep 27, 2017
to get lanuchpad's description reports' text
and check for secuirty key words
'''
from launchpadlib.launchpad import Launchpad
import numpy as np
cachedir  = '/Users/akond/.launchpadmat/'
launchpad = Launchpad.login_anonymously('LPAD_DESC_DLOAD', 'production', cachedir, version='devel')
launchpad_file_name = 'ost.bug.ids.txt'
sec_kw_file_name    = 'sec.kws.txt'
# not_exist_list = [10179904, 10131433, 1021152, 1021519, 1037104, 1041577, 1060410]
counter = 0


if __name__=='__main__':
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
   lpad_ids = [1289631]
   valid_lpad_cnt = len(lpad_ids)
   print 'before filtering:{}, after filtering:{}'.format(len(content), valid_bug_cnt)
   for lpad_id in lpad_ids:
       counter += 1
       try:
          the_lpad    =  launchpad.bugs[lpad_id]
          lpad_mesg   =  the_lpad.description
          lpad_mesg   =  [token_.strip() for token_ in lpad_mesg]
          lpad_mesg   =  [token_.lower() for token_ in lpad_mesg]
        #   common =  len(set(lpad_mesg).intersection(sec_kw_content))
        #       if (common > 0):
        #          print 'FOUND STH!!!'
        #          print 'ID:{},BUGMESSAGE:{}'.format(lpad_id,lpad_mesg)
        #          print '*'*25
          print lpad_mesg
          print '='*50
          print "Processed {} bug IDs, {} left".format(counter, valid_bug_cnt - counter)
          print '='*50
       except Exception as e:
          print 'Caught exception for:', str(lpad_id) + ':' + e.message
