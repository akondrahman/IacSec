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
    ## the previosu conditions have to be removded as now we dont have any Puppet files in spec or acceptance directories
    if ((file_path.count(constants.DOT) == 1)): 
    # if ((file_path.count(constants.DOT) == 1) and (constants.TEST_DIR_SPEC not in file_path) and (constants.TEST_DIR_ACCE not in file_path)):
    # if ((file_path.count(constants.DOT) <= 5) and (constants.TEST_DIR_SPEC not in file_path) and (constants.TEST_DIR_ACCE not in file_path)):
        flag2ret  = True
    return flag2ret

def buildOutput(output_tuple, file_name):
    str_out = ''
    for elem in output_tuple:
        str_out = str_out + str(elem) + ','
    str2ret = file_name + ',' + str_out + '\n'
    return str2ret


def getMonthData(file_p, dir_p):
    temp_     = file_p.replace(dir_p, '')
    time_dir  = temp_.split('/')[0]
    if '-' in time_dir:
       time_list = time_dir.split('-')
       month2ret = time_list[-2] + '-' + time_list[-1] + ','
    else:
       month2ret = '2019-03'
    return month2ret

def buildSymOut(sym_tup_par, mon_par, fil_par):
    type_dict = {0:constants.LINT_HARD,
                 1:constants.LINT_SUSP,
                 2:constants.LINT_SECRET,
                 3:constants.LINT_MD5,
                 4:constants.LINT_HTTP,
                 5:constants.LINT_BIND,
                 6:constants.LINT_EMPT,
                 7:constants.LINT_DEF_ADM,
                 8:constants.LINT_BASE64,
                 9:constants.LINT_MIS_DEFAU,
                 10:constants.LINT_HARD_CODE_UNAME,
                 11:constants.LINT_HARD_CODE_PASS,
                 12:constants.LINT_INTEG_VIO 
                }
    # str2ret   = ''
    list_ = []
    # print sym_tup_par
    for ind_ in xrange(len(sym_tup_par)):
        type_str=type_dict[ind_]
        str_list=sym_tup_par[ind_]
        # print str_list
        for str_ in str_list:
            # str2ret = str2ret + mon_par + ',' + fil_par + ',' + type_str + ',' + str_ + ',' + '\n'
            tup_ = (mon_par, fil_par, type_str, str_)
            list_.append(tup_)
    return list_

def sniffSmells(path_to_dir):
    counter = 0
    final_str = ''
    all_sym_list = []
    for root_, dirs, files_ in os.walk(path_to_dir):
       for file_ in files_:
           if (file_.endswith(constants.PP_EXT) or file_.endswith(constants.CH_EXT)):
                 full_p_file = os.path.join(root_, file_)
                 # for analyzing Puppet scripts
                 if (os.path.exists(full_p_file) and checkValidity(full_p_file) and (full_p_file.endswith(constants.CH_EXT)==False)):
                    counter += 1 
                    print 'Analyzing:{},Index:{}'.format(full_p_file, counter)
                    month_str      = getMonthData(full_p_file, path_to_dir)
                    secu_lint_outp = lint_engine.runLinter(full_p_file)
                    lint_cnt_out   = secu_lint_outp[0]
                    lint_cnt_str   = buildOutput(lint_cnt_out, full_p_file)
                    final_str      = final_str + month_str + lint_cnt_str
                    # print secu_lint_outp
                    '''
                     for same/new checking data
                    '''
                    symbol_out   = secu_lint_outp[1] # a tuple, where each element is a list of strs
                    per_file_sym = buildSymOut(symbol_out, month_str, full_p_file)
                    all_sym_list = all_sym_list + per_file_sym
                 # for analyzing Chef scripts
                 elif (os.path.exists(full_p_file) and ((constants.CH_DIR_RECIPE in full_p_file) or (constants.CH_DIR_COOKBOOK in full_p_file)) and (full_p_file.endswith(constants.CH_EXT)==True)):
                     counter += 1
                     print 'Analyzing:{},Index:{}'.format(full_p_file, counter)
                     month_str      = getMonthData(full_p_file, path_to_dir)
                     secu_lint_outp = lint_engine.runLinter(full_p_file)
                     lint_cnt_out   = secu_lint_outp[0]
                     lint_cnt_str   = buildOutput(lint_cnt_out, full_p_file)
                     final_str      = final_str + month_str + lint_cnt_str
                     '''
                     for same/new checking data
                     '''
                     symbol_out   = secu_lint_outp[1] # a tuple, where each element is a list of strs
                     per_file_sym = buildSymOut(symbol_out, month_str, full_p_file)
                     all_sym_list = all_sym_list + per_file_sym
                 else:
                     print "Not analyzing, failed validity checks:", full_p_file
                 print "="*50
    return final_str, all_sym_list
