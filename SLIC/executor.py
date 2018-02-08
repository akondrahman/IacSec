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
    if (('.' not in file_path) and ('spec' not in file_path)):
        flag2flag2ret  = True
    return flag2flag2ret

def sniffSmells(path_to_dir):
    for root_, dirs, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if file_.endswith(constants.PP_EXT) or file_.endswith(constants.CH_EXT):
             if checkValidity(file_):
                print "Started analyzing:", os.path.join(root_, file_)
             else:
                print "Not analyzing, failed validity checks:", os.path.join(root_, file_)
             print "="*50
