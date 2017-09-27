'''
Akond Rahman
Sep 27, 2017
to get bugzilla reports' text
and check for secuirty key words
'''
#import bugzilla
import bugsy
bugzilla_obj = bugsy.Bugsy(api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
if __name__=='__main__':
   #bug_obj = bugzilla.Bugzilla(url="https://bugzilla.mozilla.org/rest/", api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
   #URL = "https://partner-bugzilla.redhat.com"
   #bug_obj = bugzilla.Bugzilla(URL, api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")

   the_bug = bugzilla_obj.get_bug(427301)  #put numeric ID here
   bug_kws = the_bug[keywords]
   print bug_kws
   print '='*50
   comments = the_bug.get_comments()
   for comment_obj in comments():
       print comment_obj.text
   print '='*50
