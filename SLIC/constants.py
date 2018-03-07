'''
Akond Rahman
Feb 08, 2018
This file holds all constants
'''

PP_EXT = '.pp'
CH_EXT = '.rb'
CH_DIR = 'recipes'
TEST_DIR_SPEC = 'spec/'
TEST_DIR_ACCE = 'acceptance/'
DOT = '.'
EXCEPTION = 'EXCEPTION:::'
BASH_CMD  = 'bash'
BASH_FLAG = '-c'
### PUPPET LINT AND ITS RULES
PP_LINT_TOOL = 'puppet-lint -l'
PP_RULE_HARDCODE  = '../SPrules4pupp/no_hardcode_key.rb'
PP_RULE_SUSP_COMM = '../SPrules4pupp/no_susp_comments.rb'
PP_RULE_SECR_LOCA = '../SPrules4pupp/no_secret_location.rb'
PP_RULE_MD5       = '../SPrules4pupp/no_md5.rb'
PP_RULE_HTTP      = '../SPrules4pupp/no_http.rb'
PP_RULE_BIND      = '../SPrules4pupp/no_full_binding.rb'
PP_RULE_EMPTY_PWD = '../SPrules4pupp/no_empty_pwd.rb'
#### CHEF ZONE
### PUPPET LINT AND ITS RULES
CHEF_LINT_TOOL = 'foodcritic -I'
# CHEF_RULE_HARDCODE  = '../SPrules4pupp/no_hardcode_key.rb'
CHEF_ALL_RULES = '../SPrules4chef/my-rules/my_rules.rb'

###### FOLLOWING APPLICABLE FOR CHEF AND PUPPET
### OUTPUT TMP LOG
REDIRECT_NEW = '>'
REDIRECT_APP = '>>'
OUTPUT_TMP_LOG = 'TMP.LOG'
### LINT OUTPUT PARSING
LINT_SUSP   ='SECURITY:::SUSPICOUS_COMMENTS:::'
LINT_HARD   ='SECURITY:::HARD_CODED_SECRET_'
LINT_SECRET ='SECURITY:::EXPOSING_SECRET_LOCATION:::'
LINT_MD5    ='SECURITY:::MD5:::'
LINT_HTTP   ='SECURITY:::HTTP:::'
LINT_BIND   ='SECURITY:::BINDING_TO_ALL:::'
LINT_EMPT   ='SECURITY:::EMPTY_PASSWORD:::'
NEWLINE = '\n'
