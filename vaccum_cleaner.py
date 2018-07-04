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

if __name__=='__main__':
   # the_dir = '/Users/akond/SECU_REPOS/test-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/mozi-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/ostk-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/wiki-pupp/'
   # the_dir = '/Users/akond/SECU_REPOS/ghub-pupp/'

   doCleanUp(the_dir)
