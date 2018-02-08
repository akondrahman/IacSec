'''
Akond Rahman
Feb 08, 2018
Puppet Lint Engine
'''
import constants
import subprocess
import os

def generateOutput(path2file):
    # puppet-lint -l /Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/IacSec/SPrules4pupp/no_hardcode_key.rb relabs-puppet-2011-09/manifests/nodes.pp
    try:
        command2exec = constants.PP_LINT_TOOL + ' ' + constants.PP_RULE_HARDCODE + ' ' + path2file + ' ' + constants.REDIRECT + ' ' + constants.OUTPUT_TMP_LOG
        subprocess.check_output(command2exec)
    except subprocess.CalledProcessError as e:
        print constants.EXCEPTION + e.output

def runLinter(full_path_file):
    #1. run linter with custom rules
    generateOutput(full_path_file)
    num_lines = sum(1 for line_ in open(constants.OUTPUT_TMP_LOG))
    print 'Genrated a log file of {} lines'.format(num_lines)
    #2. parse output
