'''
Akond Rahman
Sep 27, 2017
to get bugzilla reports' text
and check for secuirty key words
'''
import bugzilla


if __name__=='__main__':

bug_obj = bugzilla.Bugzilla(url="https://bugzilla.mozilla.org/rest/", api_key="mWYEjiA4nOsii23LqFSuhotZyXJic5hRmMc5bFdm")
the_bug = bug_obj.get_bug(1189311)  #put numeric ID here
for bug_key, bug_vals in the_bug.iteritems(): 
        print bug_key, bug_vals
        print '='*50
