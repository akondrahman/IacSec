'''
Akond Rahman
Feb 08, 2018
Executor : detects the script type, and triggers the linter
'''
import os
import constants

def checkValidity(file_path):
    # skip files that are in hidden directories, and in spec folders
    flag2ret = False
    if ((file_path.count(constants.DOT) == 1) and (constants.TEST_DIR_SPEC not in file_path) and (constants.TEST_DIR_ACCE not in file_path)):
        flag2ret  = True
    return flag2ret

def sniffSmells(path_to_dir):
    for root_, dirs, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if file_.endswith(constants.PP_EXT) or (file_.endswith(constants.CH_EXT) and (constants.CH_DIR in file_)):
             if checkValidity(file_):
                print "Started analyzing:", os.path.join(root_, file_)
             else:
                print "Not analyzing, failed validity checks:", os.path.join(root_, file_)
             print "="*50
