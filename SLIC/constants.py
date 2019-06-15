'''
Akond Rahman
Feb 08, 2018
This file holds all constants
'''

PP_EXT = '.pp'
CH_EXT = '.rb'
CH_DIR_RECIPE   = 'recipes' 
CH_DIR_COOKBOOK = 'cookbooks'  
TEST_DIR_SPEC = 'spec/'
TEST_DIR_ACCE = 'acceptance/'
DOT = '.'
EXCEPTION = 'EXCEPTION:::'
BASH_CMD  = 'bash'
BASH_FLAG = '-c'
HIDDEN_GIT = '/.git/'
### PUPPET LINT AND ITS RULES
PP_LINT_TOOL = 'puppet-lint -l'
PP_RULE_HARDCODE  = '../SPrules4pupp/no_hardcode_key.rb'
PP_RULE_SUSP_COMM = '../SPrules4pupp/no_susp_comments.rb'
PP_RULE_SECR_LOCA = '../SPrules4pupp/no_secret_location.rb'
PP_RULE_MD5       = '../SPrules4pupp/no_md5.rb'
PP_RULE_HTTP      = '../SPrules4pupp/no_http.rb'
PP_RULE_BIND      = '../SPrules4pupp/no_full_binding.rb'
PP_RULE_EMPTY_PWD = '../SPrules4pupp/no_empty_pwd.rb'
PP_RULE_DEFAU_ADM = '../SPrules4pupp/no_default_admin.rb'
PP_RULE_BASE64    = '../SPrules4pupp/no_base64.rb'
PP_RULE_ALL_IN_ONE= '../SPrules4pupp/all_in_one.rb'  ### ultimately we are using this 
NO_OF_RULES       = 9

#### CHEF ZONE
### PUPPET LINT AND ITS RULES
CHEF_LINT_TOOL = 'foodcritic -I'
# CHEF_RULE_HARDCODE  = '../SPrules4pupp/no_hardcode_key.rb'
CHEF_ALL_RULES = '../SPrules4chef/my-rules/my_rules.rb'
CHEF_SWITCH_RULE = '../SPrules4chef/my-rules/special_missing_case.rb'

###### FOLLOWING APPLICABLE FOR CHEF AND PUPPET
### OUTPUT TMP LOG
REDIRECT_NEW = '>'
REDIRECT_APP = '>>'
OUTPUT_TMP_LOG = 'TMP.LOG'
FILE_OPEN_MODE = 'rU'
### LINT OUTPUT PARSING
LINT_SUSP      ='SECURITY:::SUSPICOUS_COMMENTS:::'
LINT_HARD      ='SECURITY:::HARD_CODED_SECRET_'        # to handle 2 versions
LINT_SECRET    ='SECURITY:::EXPOSING_SECRET_LOCATION_' # to handle 2 versions
LINT_MD5       ='SECURITY:::MD5:::'
LINT_HTTP      ='SECURITY:::HTTP:::'
LINT_BIND      ='SECURITY:::BINDING_TO_ALL:::'
LINT_EMPT      ='SECURITY:::EMPTY_PASSWORD:::'
LINT_DEF_ADM   ='SECURITY:::ADMIN_BY_DEFAULT:::'
LINT_BASE64    ='SECURITY:::BASE64:::'
LINT_MIS_DEFAU ='SECURITY:::MISSING_DEFAULT:::'
LINT_INTEG_VIO ='SECURITY:::SOURCE_INTEGRITY:::'
###
PUPP_MISS_DEFA ='WARNING: case statement without a default'
#### For Hard coded secret breakdown 
LINT_HARD_CODE_UNAME ='SECURITY:::HARD_CODED_SECRET_USER_NAME:::'
LINT_HARD_CODE_PASS  ='SECURITY:::HARD_CODED_SECRET_PASSWORD:::'

NEWLINE   = '\n'
AT_SYMBOL = '@'
### HEADER STRING
puppHeaderStr1  = 'MONTH,'    + 'FILE_NAME,' + 'HARD_CODE_SECR,' + 'SUSP_COMM,' + 'SECR_LOCA,'
puppHeaderStr2  = 'MD5_USAG,' + 'HTTP_USAG,' + 'BIND_USAG,' + 'EMPT_PASS,' + 'DFLT_ADMN,'
puppHeaderStr3  = 'HARD_CODE_UNAME,' + 'HARD_CODE_PASS,' + 'BASE_64,'  + 'PUPP_MISS_DFLT,' + 'TOTAL,' 
PUPP_HEADER_STR = puppHeaderStr1 + puppHeaderStr2  + puppHeaderStr3

chefHeaderStr1  = 'MONTH,' + 'REPO_DIR,'   + 'FILE_NAME,' + 'HARD_CODE_SECR,' + 'SUSP_COMM,'
chefHeaderStr2  = 'MD5_USAG,' + 'HTTP_USAG,' + 'BIND_USAG,' + 'EMPT_PASS,' + 'DFLT_ADMN,'
chefHeaderStr3  = 'HARD_CODE_UNAME,' + 'HARD_CODE_PASS,' + 'CHEF_MISS_DFLT,' + 'INTE_CHCK,'  + 'TOTAL,'
CHEF_HEADER_STR = chefHeaderStr1 + chefHeaderStr2 + chefHeaderStr3

SYM_HEAD   = 'MONTH,FILE,SYMBOL,TYPE'

ALREADY_VISITED_LOCATION = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/IacSec/SLIC/TEMP_DATA_HOLDER.csv'
TEMP_HOLDER = 'TEMP_DATA_HOLDER.csv'
ALREADY_VISITED_FIELD = 'FILE_NAME'
PATH_SPLITTER = '/'
PATH_INDEX = 6
