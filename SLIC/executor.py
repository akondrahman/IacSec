'''
Akond Rahman
Feb 08, 2018
Executor : detects the script type, and triggers the linter
'''
import os
import constants
import lint_engine

def checkValidity(file_path):
    # skip files that are in hidden directories, and in spec folders
    flag2ret = False
    if ((file_path.count(constants.DOT) == 1) and (constants.TEST_DIR_SPEC not in file_path) and (constants.TEST_DIR_ACCE not in file_path)):
        flag2ret  = True
    return flag2ret

def sniffSmells(path_to_dir):
    for root_, dirs, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if (file_.endswith(constants.PP_EXT) or file_.endswith(constants.CH_EXT)):
                 full_p_file = os.path.join(root_, file_)
                 if (os.path.exists(full_p_file) and checkValidity(full_p_file) and (full_p_file.endswith(constants.CH_EXT)==False)):
                    print 'Analyzing:', full_p_file
                    secu_lint_outp = lint_engine.runLinter(full_p_file)
                    print secu_lint_outp
                 elif (os.path.exists(full_p_file) and (constants.CH_DIR in full_p_file) and (full_p_file.endswith(constants.PP_EXT)==False)):
                    print 'Analyzing:', full_p_file
                    secu_lint_outp = lint_engine.runLinter(full_p_file)
                    print secu_lint_outp
                 else:
                    print "Not analyzing, failed validity checks:", full_p_file
                 print "="*50
