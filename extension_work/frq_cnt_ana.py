'''
Akond Rahman
Frequency count : Journal 
April 07, 2019 
'''
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os

def createOutputDirectory(dirParam):
  if not os.path.exists(dirParam):
     os.makedirs(dirParam)

def calcSmellDensity(smell_cnt, file_list):
    val = 0
    tot_lin = 0
    for file_path in file_list:
        file_ = open(file_path, 'rU')
        num_lines = sum(1 for line_ in file_)
        tot_lin = tot_lin + num_lines
    smell_density = float(smell_cnt)/float(tot_lin)
    val = round(smell_density * 1000, 3) ### density per KLOC
    return val

def sortDate(mon_lis):
    months = [datetime.datetime.strptime(m, "%Y-%m") for m in mon_lis]
    months.sort()
    sorted_mon = [datetime.datetime.strftime(m_, "%Y-%m") for m_ in months]
    return sorted_mon

def makePlot(x_par, y_par, head_par, out_dir_par, type_par, ds_par):
    plt_x_axis = [x_ for x_ in xrange(len(x_par))]
    plt.xticks(plt_x_axis, x_par)
    plt.plot(plt_x_axis, y_par)
    plt.title(head_par)
    plt.xlabel('MONTH')
    plt.ylabel(type_par)
    #plt.show()
    file2save = out_dir_par + head_par + '_' + type_par + '_' + ds_par + '.png'
    plt.savefig(file2save)
    plt.close()

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

def makeCSV(lis_par, nam, dir):
    str_ = ''
    header = 'MONTH,TYPE,CNT_PER_FIL,SMELL_DENSITY,UNI_FIL_PER,'
    for tup in lis_par:
        for elem in tup:
            str_ = str_ + str(elem) + ','
        str_ = str_ + '\n'
    str_ = header + '\n' + str_
    file2save = dir + nam + '.csv'
    os_bytes = dumpContentIntoFile(str_, file2save)
    print 'DUMPED CSV FILE OF {} BYTES'.format(os_bytes)

def perfAnal(df_pa, header_pa, ds_name):
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    mon_lis = sortDate(mon_lis)
    csv_list = []
    for head_ in header_pa:
        '''
        for summary puprpose
        '''
        stat_list = df_pa[head_].tolist()
        # print 'DATASET:{},SMELL:{},MIN:{},MEDIAN:{},MAX:{}'.format(ds_nam, head_, min(stat_list), np.median(stat_list), max(stat_list))
        uni_fil_lis, mon_plt_lis, cnt_plt_lis, sme_den_lis = [], [], [], []
        for mon_ in mon_lis:
            mon_df = df_pa[df_pa['MONTH']==mon_]
            per_mon_per_smell_list = mon_df[head_].tolist()
            per_mon_cnt = sum(per_mon_per_smell_list) # we need the total count

            per_mon_fil = mon_df['FILE_NAME'].tolist() # we need all file names, a smell can appear multiple times in a file

            per_mon_fil_cnt = len(np.unique(per_mon_fil)) #  file count
            cnt_per_fil   = round(float(per_mon_cnt)/float(per_mon_fil_cnt), 3)
            smell_density = calcSmellDensity(per_mon_cnt, per_mon_fil)
            # print 'MON:{}, CNT:{}, FIL:{}, CNT_PER_FIL:{}, SMELL_DENS:{}, TYPE:{}'.format(mon_, per_mon_cnt, per_mon_fil_cnt, cnt_per_fil, smell_density, head_)
            ## CNT_PER_FILE is an interesting metric, which will not be used now , but for future. 
            # print '-'*25
            ### code for PROPORTION metric 
            at_least_one_files = np.unique( mon_df[mon_df[head_] > 0 ]['FILE_NAME'].tolist() )
            all_files          = np.unique( mon_df['FILE_NAME'].tolist() )
            prop_metric        = round(float(len(at_least_one_files)) / float(len(all_files)), 5) * 100 
            print 'MON:{}, AT_LEAST_ONE_CNT:{}, ALL_FILE_CNT:{}, SMELL_DENS:{}, PROP:{}, TYPE:{}'.format(mon_, len(at_least_one_files), len(all_files), smell_density, prop_metric , head_)
            print '-'*25

if __name__=='__main__':
   '''
   pass the needed column headers
   '''
   needed_header = ['HARD_CODE_SECR',	'SUSP_COMM',	'MD5_USAG',
                    'HTTP_USAG',	'BIND_USAG',	'EMPT_PASS',	'DFLT_ADMN',
                    'HARD_CODE_UNAME', 'HARD_CODE_PASS', 
                    'MISS_DFLT', 'INTE_CHCK', 'TOTAL']


#    results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_GHUB_SLIC_CHEF.csv'
#    results_df   = pd.read_csv(results_file)
#    ds_nam = 'GITHUB'

#    results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V1_ALL_OSTK_CHEF.csv'
#    results_df   = pd.read_csv(results_file)
#    ds_nam = 'OPENSTACK'

   perfAnal(results_df, needed_header, ds_nam)
   print '='*100 
   print 'The dataset was:', results_file
   print '='*100 
