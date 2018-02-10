'''
Akond Rahman
Feb 10, 2018
Sat
Code to geenrate data
'''
import os

def checkValidity(file_path):
    # skip files that are in hidden directories, and in spec folders
    flag2ret = False
    if ((file_path.count('.') == 1) and ('spec' not in file_path) and ('acceptance' not in file_path)):
        flag2ret  = True
    return flag2ret

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

def generateData(path_to_dir):
    str2ret = ''
    for root_, dirs_, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if (file_.endswith('.pp') or file_.endswith('.rb')):
                 tmp_month_str = root_.split('/')[5]
                 if '-' in tmp_month_str:
                    month_str = tmp_month_str.split('-')[-2] + '-' + tmp_month_str.split('-')[-1]
                    full_p_file = os.path.join(root_, file_)
                    if (os.path.exists(full_p_file) and checkValidity(full_p_file) and (full_p_file.endswith('.rb')==False)):
                       # print 'Analyzing:', full_p_file, month_str
                       str2ret = str2ret + full_p_file + ',' + month_str + ',' + '\n'
                    elif (os.path.exists(full_p_file) and ('recipes' in full_p_file) and (full_p_file.endswith('.pp')==False)):
                       # print 'Analyzing:', full_p_file, month_str
                       str2ret = str2ret + full_p_file + ',' + month_str + ',' + '\n'
    return str2ret


if __name__=='__main__':
   ds_path  = '/Users/akond/SECU_REPOS/test-pupp/'
   out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/IacSec/sampling/test.csv'


   str2Dump = generateData(ds_path)
   str2Dump = 'FILE,' + 'MONTH,' + '\n' + str2Dump 
   out_byt  = dumpContentIntoFile(str2Dump, out_file)
   print 'Dumped a file of {} bytes'.format(out_byt)
