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
    rulesToCheck = [constants.PP_RULE_HARDCODE, constants.PP_RULE_SUSP_COMM]
    for rule_ in rulesToCheck:
        ##
        command2exec = constants.PP_LINT_TOOL + ' ' + rule_ + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
        try:
           # print command2exec
           subprocess.check_output(['bash','-c', command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)
        # raise RuntimeError("command '{}' return with error (code {}): {}".format(e_.cmd, e_.returncode, e_.output))

def runLinter(full_path_file):
    #1. run linter with custom rules
    generateOutput(full_path_file)
    num_lines = sum(1 for line_ in open(constants.OUTPUT_TMP_LOG))
    print 'Genrated a log file of {} lines'.format(num_lines)
    #2. parse output
    #3. delete temp file
    os.remove(constants.OUTPUT_TMP_LOG)
