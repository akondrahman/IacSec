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
        smell_density = float(all_smell_cnt)/float(tot_loc)
        print smell_name + ',' + str(round(smell_density, 5))

def getOccurences(mon_df):
    files  = np.unique( mon_df['FILE_NAME'].tolist() )
    features = mon_df.columns
    dropcols = ['MONTH', 'FILE_NAME', 'Unnamed']
    smell_names = [x_ for x_ in features if x_ not in dropcols]
    for smell_name in smell_names:
        all_smell_cnt = sum(mon_df[smell_name].tolist())
        print smell_name , all_smell_cnt

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
    print 'SMELL DENSITY'
    print '='*50
    getSmellDensity(mon_df)
    print '='*100
    print 'AT LEAST ONCE'
    print '='*50
    getAppearance(mon_df)
    print '='*100
    print 'OCCURRENCES'
    print '='*50
    getOccurences(mon_df)
    print '='*100


def getRepoLink(repo_src, df_):
    #/Users/akond/SECU_REPOS/ghub-pupp/puppet-sonarqube-2017-11/tests/runner.pp
    file_names = df_['FILE_NAME'].tolist()    
    for file_ in file_names:
        relative_name = file_.replace(repo_src, '')
        folder_name = relative_name.split('/')[0]
        y_m = folder_name.split('-')
        y_, m_ = y_m[-2], y_m[-1]
        month_str = '-' + y_ + '-' + m_
        repo_name = folder_name.replace(month_str, '')
        print relative_name, repo_name

if __name__=='__main__':
   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_GITHUB_PUPPET.csv'
   result_df = pd.read_csv(results_file)
   the_month = '2018-06'
   #mineMonthData(result_df, the_month)

   '''
   for Github issues
   '''
   repo_dir = '/Users/akond/SECU_REPOS/ghub-pupp/'
   getRepoLink(repo_dir, result_df)