'''
Akond Rahman
July 04, 2018
Clean up files you don't need
'''
import os

def doCleanUp(dir_name):
    pp_, non_pp = [], []
    for root_, dirs, files_ in os.walk(dir_name):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if(os.path.exists(full_p_file)):
             if (full_p_file.endswith('.pp')):
               pp_.append(full_p_file)
             else:
               non_pp.append(full_p_file)
    for f_ in non_pp:
        os.remove(f_)
    print "="*50
    print dir_name
    print 'removed {} non-puppet files, kept {} Puppet files #savespace '.format(len(non_pp), len(pp_))
    print "="*50

def getCount(dir_name, the_mon):
    pp_, non_pp = [], []
    for root_, dirs, files_ in os.walk(dir_name):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if((os.path.exists(full_p_file)) and (the_mon in full_p_file)):
             if (full_p_file.endswith('.pp')):
               pp_.append(full_p_file)
             else:
               non_pp.append(full_p_file)    

    print 'DIR:{},Puppet:{}, Non-Puppet:{}, Total:{}'.format(dir_name, len(pp_), len(non_pp), len(pp_) + len(non_pp))

if __name__=='__main__':
   # the_dir = '/Users/akond/SECU_REPOS/test-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/mozi-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/ostk-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/wiki-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/ghub-pupp/'

   #doCleanUp(the_dir)
   # the_dir = '/Users/akond/PUPP_REPOS/mozilla-releng-downloads/extra_repos_icse19/'
   # the_dir = '/Users/akond/PUPP_REPOS/openstack-downloads/extra_repos_icse19/'
   # the_dir = '/Users/akond/PUPP_REPOS/wikimedia-downloads/extra_repos_icse19/'
   # getCount(the_dir, '2018-06')
