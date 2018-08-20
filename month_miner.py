'''
Month speicifc result miner
Akond Rahman
July 01, 2018
'''
import pandas as pd
import numpy as np
import os

def getSmellDensity(mon_df):
    files  = np.unique( mon_df['FILE_NAME'].tolist() )
    tot_loc = 0
    for file_ in files:
        if os.path.exists(file_):
           tot_loc = tot_loc + sum(1 for line in open(file_))

    features = mon_df.columns
    dropcols = ['MONTH', 'FILE_NAME']
    smell_names = [x_ for x_ in features if x_ not in dropcols]
    for smell_name in smell_names:
        all_smell_cnt = sum(mon_df[smell_name].tolist())
        smell_density = float(all_smell_cnt)/(float(tot_loc) / float(1000))
        print smell_name + ',' + str(round(smell_density, 5))
    return tot_loc

def getOccurences(mon_df):
    files  = np.unique( mon_df['FILE_NAME'].tolist() )
    features = mon_df.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed']
    smell_names = [x_ for x_ in features if x_ not in dropcols]
    for smell_name in smell_names:
        all_smell_cnt = sum(mon_df[smell_name].tolist())
        print smell_name , all_smell_cnt
    return len(files)

def getAppearance(mon_df):
    ## at least one count
    features = mon_df.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed']
    smell_names = [x_ for x_ in features if x_ not in dropcols]
    for smell_name in smell_names:
        #print mon_df.head()
        all_fil_cnt = len(np.unique(mon_df['FILE_NAME'].tolist()))
        appear_cnt  = len(np.unique(mon_df[mon_df[smell_name] > 0]['FILE_NAME'].tolist()))
        dis_appear_cnt = len(np.unique(mon_df[mon_df[smell_name] <= 0]['FILE_NAME'].tolist()))
        at_least_one_perc = (round(float(appear_cnt)/float(all_fil_cnt), 5)) * 100
        print "Smell:{}, ATLEASTONE_COUNT:{}, NONE:{}, TOTALFILE_COUNT:{}, ATLEASTONE_PERC:{}".format(smell_name , appear_cnt, dis_appear_cnt, all_fil_cnt, at_least_one_perc)

def mineMonthData(df_param, mo_param):
    mon_df = df_param[df_param['MONTH']==mo_param]
    print '='*100
    print 'SMELL DENSITY (PER KLOC)'
    print '='*50
    tot_loc = getSmellDensity(mon_df)
    print '='*50
    print 'TOTAL LOC:', tot_loc
    print '='*100
    print 'AT LEAST ONCE'
    getAppearance(mon_df)
    print '='*100
    print 'OCCURRENCES'
    print '='*100
    print '='*50
    file_count = getOccurences(mon_df)
    print 'TOTAL SCRIPT COUNT:', file_count
    print '='*50
    print '='*100


def getRepoLink(repo_src, df_, metadata_df, mo_param, smell_to_look):
    tracker = []
    #/Users/akond/SECU_REPOS/ghub-pupp/puppet-sonarqube-2017-11/tests/runner.pp
    mon_df = df_[df_['MONTH']==mo_param]
    valid_df = mon_df[mon_df[smell_to_look] > 0 ]
    file_names = valid_df['FILE_NAME'].tolist()    
    for file_ in file_names:
        relative_name = file_.replace(repo_src, '')
        folder_name = relative_name.split('/')[0]
        pp_file_name   = relative_name.replace(folder_name, '')
        y_m = folder_name.split('-')
        y_, m_ = y_m[-2], y_m[-1]
        month_str = '-' + y_ + '-' + m_
        repo_name = folder_name.replace(month_str, '')
        repo_json_file =  repo_name + '.json'
        #print relative_name, repo_json_file
        if repo_json_file not in tracker:
            selected_df = metadata_df[metadata_df['dir_name']==repo_json_file]
            non_fork_df = selected_df[selected_df['fork?']==0]
            watcher_filtered_df = non_fork_df[non_fork_df['watchers'] > 1]
            repo_ = watcher_filtered_df['repo_name'].tolist()[0].split('.')[0]
            smell_df = valid_df[valid_df['FILE_NAME']==file_]
            direct_url = 'https://github.com/' + repo_ + '/' + 'blob/master' + pp_file_name
            print repo_json_file + ',' + repo_  + ',' + pp_file_name + ',' + direct_url + ',' + file_
            #print smell_df
            #print '='*50
            tracker.append(repo_json_file)

def getFileName(df_param, mo_param, smell_param):
    str_ = ''
    mon_df   = df_param[df_param['MONTH']==mo_param]  
    #print mon_df.head()
    smell_df = mon_df[mon_df[smell_param] > 0]
    smell_df.to_csv('SMELL_DF_OUTPUT.csv')
    #print smell_df.head()
    files_with_smells = np.unique(smell_df['FILE_NAME'].tolist())
    for file_name in files_with_smells:
      str_ = str_ + file_name + ',' + '\n'
    return str_

if __name__=='__main__':
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_GITHUB_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_MOZILLA_PUPPET.csv'
   #results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_OPENSTACK_PUPPET.csv'
   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_OUTPUT/V10_ALL_WIKIMEDIA_PUPPET.csv'
   

   result_df = pd.read_csv(results_file)
   the_month = '2018-06'
   print '='*100
   print results_file
   print '='*100
   # mineMonthData(result_df, the_month)

   '''
   for Github issues
   '''
   SMELL_TO_LOOK = 'SUSP_COMM'
   repo_dir = '/Users/akond/SECU_REPOS/ghub-pupp/'
   repo_name_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/metadata_output.csv'
   repo_name_df = pd.read_csv(repo_name_file)
   #print repo_name_df.head()
   #getRepoLink(repo_dir, result_df, repo_name_df, the_month, SMELL_TO_LOOK)


   '''
   for Openstack and Wikimedia Bug Reports 
   '''
   SMELL_TO_LOOK = 'HTTP_USAG'
   result_df = pd.read_csv(results_file)
   str_ = getFileName(result_df, the_month, SMELL_TO_LOOK)   
   print str_