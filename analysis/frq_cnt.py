'''
Akond Rahman
Smell count per script
Mar 17, 2018
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
    val = round(float(smell_cnt)/float(tot_lin), 3)
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
    header = 'MONTH,TYPE,CNT_PER_FIL,SMELL_DENSITY,'
    for tup in lis_par:
        for elem in tup:
            str_ = str_ + str(elem) + ','
        str_ = str_ + '\n'
    str_ = header + '\n' + str_
    file2save = dir + nam + '.csv'
    os_bytes = dumpContentIntoFile(str_, file2save)
    print 'DUMPED CSV FILE OF {} BYTES'.format(os_bytes)

def perfAnal(df_pa, header_pa, output_dir, ds_name):
    createOutputDirectory(output_dir)
    mon_lis = np.unique(df_pa['MONTH'].tolist())
    mon_lis = sortDate(mon_lis)
    csv_list = []
    for head_ in header_pa:
        mon_plt_lis, cnt_plt_lis, sme_den_lis = [], [], []
        for mon_ in mon_lis:
            mon_df = df_pa[df_pa['MONTH']==mon_]
            per_mon_cnt = sum(mon_df[head_].tolist()) # we need the total count
            per_mon_fil = np.unique(mon_df['FILE_NAME'].tolist()) # we need the unique file names
            per_mon_fil_cnt = len(per_mon_fil) # unque file count
            cnt_per_fil   = round(float(per_mon_cnt)/float(per_mon_fil_cnt), 3)
            smell_density = calcSmellDensity(per_mon_cnt, per_mon_fil)
            print 'MON:{}, CNT:{}, FIL:{}, CNT_PER_FIL:{}, SMELL_DENS:{}, TYPE:{}'.format(mon_, per_mon_cnt, per_mon_fil_cnt, cnt_per_fil, smell_density, head_)
            mon_plt_lis.append(mon_)
            cnt_plt_lis.append(cnt_per_fil)
            sme_den_lis.append(smell_density)
            print '*'*25
            csv_list.append((mon_, head_, cnt_per_fil, smell_density))
        makePlot(mon_plt_lis, cnt_plt_lis, head_, output_dir, 'CNT_PER_FIL', ds_name)
        makePlot(mon_plt_lis, sme_den_lis, head_, output_dir, 'SMELL_DENSITY', ds_name)
        print '='*50
    makeCSV(csv_list, ds_name, output_dir)

if __name__=='__main__':
   '''
   pass the needed colun headers
   '''
   needed_header = ['HARD_CODE_SECR',	'SUSP_COMM',	'SECR_LOCA',	'MD5_USAG',
                    'HTTP_USAG',	'BIND_USAG',	'EMPT_PASS',	'DFLT_ADMN',
                    'BASE_64',	'MISS_DFLT',	'TOTAL']

   # results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_TEST_PUPPET.csv'
   # results_df   = pd.read_csv(results_file)
   # plot_out_dir = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3/'
   # ds_name = 'TEST'

   results_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V3_OUTPUT/V3_ALL_WIKIMEDIA_PUPPET.csv'
   results_df   = pd.read_csv(results_file)
   plot_out_dir = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v3_wik/'
   ds_nam = 'WIKIMEDIA'

   perfAnal(results_df, needed_header, plot_out_dir, ds_nam)
