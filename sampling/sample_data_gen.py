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

def generateData(path_to_dir):
    for root_, dirs_, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if (file_.endswith('.pp') or file_.endswith('.rb')):
                 tmp_month_str = root_.split('/')[4]
                 month_str = tmp_month_str.split('-')[-2] + '-' + tmp_month_str.split('-')[-1]
                 full_p_file = os.path.join(root_, file_)
                 if (os.path.exists(full_p_file) and checkValidity(full_p_file) and (full_p_file.endswith('.rb')==False)):
                    print 'Analyzing:', full_p_file, month_str
                 elif (os.path.exists(full_p_file) and ('recipes' in full_p_file) and (full_p_file.endswith('.pp')==False)):
                    print 'Analyzing:', full_p_file, month_str

if __name__=='__main__':
   ds_path = '/Users/akond/SECU_REPOS/test-pupp/'
   generateData(ds_path)
