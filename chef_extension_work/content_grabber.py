'''
Akond Rahman 
Nov 21 2018 
Content Grabber for Chef Analysis 
'''
import os 
import shutil

def getFileLines(file_para):
    file_lines = []
    with open(file_para, 'rU') as log_fil:
         file_str = log_fil.read()
         file_lines = file_str.split('\n')
    file_lines = [x_ for x_ in file_lines if x_ != '\n']
    return file_lines

def grabContent(tot_fil_lis):
    tot_fil_cnt = len(tot_fil_lis)
    print 'Total files to analyze:', tot_fil_cnt
    print '-'*100
    file_counter = 0
    for file_content_tup in tot_fil_lis:
            file_content , file_name = file_content_tup
            file_counter += 1
            print '='*25 + ':'*3 + str(file_counter)   + ':'*3  + 'START!' + '='*25
            print file_name
            print '*'*10
            print file_content
            print '*'*10
            print 'DECISION===>:'
            print '*'*10
            print '='*25 + ':'*3   + str(file_counter) + ':'*3  + 'END!!!' + '='*25
    print '-'*100

def getFileContent(path_f):
    data_ = ''
    with open(path_f, 'rU') as myfile:
         data_ = myfile.read()
    return data_

def getLegitFiles(dir_par):
    chef_ = []
    for root_, dirs, files_ in os.walk(dir_par):
       for file_ in files_:
           full_p_file = os.path.join(root_, file_)
           if(os.path.exists(full_p_file)):
             if (('cookbooks' in full_p_file) and (full_p_file.endswith('.rb'))):
                file_content = getFileContent(full_p_file)
                chef_.append((file_content, full_p_file))
    return chef_
    

if __name__=='__main__':
    repo_list = ['cookbook-openstack-compute', 'cookbook-openstack-common', 'cookbook-openstack-network', 
                'cookbook-openstack-block-storage', 'cookbook-openstack-dashboard', 'cookbook-openstack-identity',
                'cookbook-openstack-image', 'cookbook-openstack-telemetry', 'cookbook-openstack-orchestration',
                 'cookbook-openstack-ops-database', 'compass-adapters', 
               ]
    all_file_lis = []
    the_root_dir = '/Users/akond/SECU_REPOS/ostk-chef/'
    repo_file = the_root_dir + 'all.openstack.repos.txt'
    repo_dirs = getFileLines(repo_file)
    for repo_ in repo_dirs:
        repo_ = repo_.replace(' ', '')
        full_dir_p = the_root_dir + repo_ + '/'
        if (os.path.exists(full_dir_p)):
            if repo_ not in repo_list: 
                shutil.rmtree( full_dir_p )
            else: 
                chef_files = getLegitFiles(full_dir_p)
                for chef_ in chef_files:
                    all_file_lis.append(chef_)
    grabContent(all_file_lis)