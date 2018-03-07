'''
Akond Rahman
Feb 08, 2018
Puppet Lint Engine
'''
import constants
import subprocess
import os

def generateOutput(path2file):
    ## Add rules to check automatically here
    if(path2file.endswith(constants.PP_EXT)):
        ## this list will be expnaded
        rulesToCheck = [constants.PP_RULE_HARDCODE, constants.PP_RULE_SUSP_COMM, constants.PP_RULE_SECR_LOCA]
        lintToolCmd = constants.PP_LINT_TOOL
    else:
        rulesToCheck = [constants.CHEF_ALL_RULES]
        lintToolCmd = constants.CHEF_LINT_TOOL
    for rule_ in rulesToCheck:
        try:
           command2exec = lintToolCmd + ' ' + rule_ + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
           # print command2exec
           subprocess.check_output([constants.BASH_CMD, constants.BASH_FLAG, command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)
        # raise RuntimeError("command '{}' return with error (code {}): {}".format(e_.cmd, e_.returncode, e_.output))

def getOutputLines():
    file_ = open(constants.OUTPUT_TMP_LOG, 'rU')
    file_str = file_.read()
    file_lines = file_str.split(constants.NEWLINE)
    return file_lines

def getHardCodeCount():
    file_lines = getOutputLines()
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HARD in s_]
    cnt2ret = sum(constants.LINT_HARD in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getSuspCommCount():
    file_lines = getOutputLines()
    line2ret = [ s_ for s_ in file_lines if constants.LINT_SUSP in s_]
    cnt2ret = sum(constants.LINT_SUSP in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getSecretLocaCount():
    file_lines = getOutputLines()
    line2ret = [ s_ for s_ in file_lines if constants.LINT_SECRET in s_]
    cnt2ret = sum(constants.LINT_SECRET in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getMD5UsageCount():
    file_lines = getOutputLines()
    line2ret = [ s_ for s_ in file_lines if constants.LINT_MD5 in s_]
    cnt2ret = sum(constants.LINT_MD5 in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def getHTTPUsageCount():
    file_lines = getOutputLines()
    line2ret = [ s_ for s_ in file_lines if constants.LINT_HTTP in s_]
    cnt2ret = sum(constants.LINT_HTTP in s_ for s_ in file_lines)
    return cnt2ret, line2ret

def parseOutput():
    '''
    Initialization
    '''
    rul_hardcode_cnt, rul_susp_comm_cnt   = 0, 0
    rul_susp_comm_cnt, rul_susp_comm_lin  = 0, 0
    rul_secr_loca_cnt, rul_secr_loca_lin  = 0, 0
    rul_md5_usage_cnt, rul_md5_usage_lin  = 0, 0
    rul_http_use_cnt,  rul_http_use_lin   = 0, 0
    '''
    '''
    num_lines = sum(1 for line_ in open(constants.OUTPUT_TMP_LOG))
    print 'Genrated a log file of {} lines'.format(num_lines)
    if num_lines > 0:
        rul_hardcode_cnt,  rul_hardcode_lin   = getHardCodeCount()
        rul_susp_comm_cnt, rul_susp_comm_lin  = getSuspCommCount()
        rul_secr_loca_cnt, rul_secr_loca_lin  = getSecretLocaCount()
        rul_md5_usage_cnt, rul_md5_usage_lin  = getMD5UsageCount()
        rul_http_use_cnt,  rul_http_use_lin   = getHTTPUsageCount()

    # this will be expanded
    output2ret = (rul_hardcode_cnt, rul_susp_comm_cnt, rul_secr_loca_cnt, rul_md5_usage_cnt, rul_http_use_cnt)
    # this will be expanded
    str2ret    = (rul_hardcode_lin, rul_susp_comm_lin, rul_secr_loca_lin, rul_md5_usage_lin, rul_http_use_lin)
    return output2ret, str2ret




def runLinter(full_path_file):
    #1. run linter with custom rules
    generateOutput(full_path_file)
    #2. parse output
    all_rul_cnt_out = parseOutput()
    #3. delete temp file
    os.remove(constants.OUTPUT_TMP_LOG)
    return all_rul_cnt_out
