'''
Akond Rahman
Sep 27, 2017
to get bugzilla reports' text
and check for secuirty key words
'''
#import bugzilla
import numpy as np
import bugsy
bugzilla_obj = bugsy.Bugsy(api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
bugzilla_file_name = 'moz.bug.ids.txt'
sec_kw_file_name   = 'sec.kws.txt'
not_exist_list = [10179904, 10131433, 1021152, 1021519, 1037104, 1041577, 1060410]

counter = 0
if __name__=='__main__':
   #bug_obj = bugzilla.Bugzilla(url="https://bugzilla.mozilla.org/rest/", api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
   #URL = "https://partner-bugzilla.redhat.com"
   #bug_obj = bugzilla.Bugzilla(URL, api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")

   with open(bugzilla_file_name) as f:
        content = f.readlines()
   with open(sec_kw_file_name) as f_:
        sec_kw_content = f_.readlines()
   sec_kw_content = [sec_kw.strip() for sec_kw in sec_kw_content]
   sec_kw_content = [sec_kw.lower() for sec_kw in sec_kw_content]
   bug_ids = [x.strip() for x in content]
   bug_ids = np.unique(bug_ids)
   bug_ids = [int(bug_id) for bug_id in bug_ids]
   bug_ids = [bug_id for bug_id in bug_ids if bug_id not in not_exist_list]
   valid_bug_cnt = len(bug_ids)
   match_cnt = 0
   print 'before filtering:{}, after filtering:{}'.format(len(content), valid_bug_cnt)
   for bug_id in bug_ids:
       counter += 1
       matching_sec_kw = 'LOL'
       sec_flag = False
       try:
          the_bug = bugzilla_obj.get(bug_id)  #put numeric ID here
          comments = the_bug.get_comments()
          for comment_obj in comments:
              comment_msg =  comment_obj.text
              for sec_kw in sec_kw_content:
                  if(sec_kw in comment_msg):
                      sec_flag = True
                      matching_sec_kw=sec_kw
          if (sec_flag):
                 match_cnt += 1
                 print 'FOUND STH!!!'
                 print 'BUGID:{},MATCHING-KW:{},MATCH-CNT:{}'.format(bug_id, matching_sec_kw, match_cnt)
                 print '*'*25
          print '='*50
          print "Processed {} bug IDs, {} left".format(counter, valid_bug_cnt - counter)
          print '='*50
       except Exception as b_e:
          print 'Caught exception for:', str(bug_id) + ':' + b_e.message
