'''
Akond Rahman
Sep 27, 2017
to get bugzilla reports' text
and check for secuirty key words
'''
#import bugzilla
import bugsy
bugzilla_obj = bugsy.Bugsy(api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
bugzilla_file_name = ''
if __name__=='__main__':
   #bug_obj = bugzilla.Bugzilla(url="https://bugzilla.mozilla.org/rest/", api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
   #URL = "https://partner-bugzilla.redhat.com"
   #bug_obj = bugzilla.Bugzilla(URL, api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")

   with open(bugzilla_file_name) as f:
        content = f.readlines()
   bug_ids = [x.strip() for x in content]
   bug_ids = [int(bug_id) for bug_id in bug_ids]
   for bug_id in bug_ids:
       #the_bug = bugzilla_obj.get(427301)  #put numeric ID here
       print bug_id
       print '='*50       
       the_bug = bugzilla_obj.get(bug_id)  #put numeric ID here
       comments = the_bug.get_comments()
       for comment_obj in comments:
           print comment_obj.text
       print '='*50
