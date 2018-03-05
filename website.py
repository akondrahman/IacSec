'''
Script to add values to database table
Akond Rahman
Nov 23, 2017
Thursday, thanksgiving day
'''
import pymysql.cursors
import cPickle as pickle
import os, csv, random

def giveConnection():
    _host = "localhost"
    _user = "root"
    _password = "Ansible#2016"
    _database = "iac"
    # Connect to the database
    _connection = pymysql.connect(host=_host,
                                 user=_user,
                                 password=_password,
                                 db=_database,
                                 cursorclass=pymysql.cursors.DictCursor)
    return _connection

def insertTableValues(path_p, content_p):
  connection = giveConnection()
  try:
    with connection.cursor() as cursor:
      tableFieldStr = "(path, content)"
      inseSttmt = "INSERT INTO `iac` " + tableFieldStr +" VALUES (%s, %s)"
      dataToInserTuple = (path_p, content_p)
      cursor.execute(inseSttmt,  dataToInserTuple)
      connection.commit()
  finally:
    connection.close()

def createPickle(ds_path_p):
    dict2dump={}
    for ds_ in ds_path_p:
        with open(ds_, 'rU') as file_:
             reader_ = csv.reader(file_)
             next(reader_, None)
             for row_ in reader_:
                 path_of_file       = row_[1]
                 if(os.path.exists(path_of_file)):
                   #print 'Processing:', path_of_file
                   file2read = open(path_of_file, 'rU')
                   fileAsStr = file2read.read()
                   if path_of_file not in dict2dump:
                      dict2dump[path_of_file] = fileAsStr

    pickle.dump(dict2dump, open('ALL_CONTENT_PICKLE.pickle', 'wb'))
    dump_status=os.stat('ALL_CONTENT_PICKLE.pickle').st_size
    print 'DUMPED A PICKLE FILE OF {} BYTES'.format(dump_status)

def insertAllData(the_pkl):
    dictOfFiles = pickle.load(open(the_pkl, 'rb'))
    for path_, content_ in dictOfFiles.iteritems():
        print content_
        print '-'*25

def insertChefData(full_ds_p_list):
    dict2dump = {}
    for path_to_dir in full_ds_p_list:
        for root_, dirs, files_ in os.walk(path_to_dir):
            for file_ in files_:
                if (file_.endswith('rb')):
                   full_p_file = os.path.join(root_, file_)
                   if (os.path.exists(full_p_file) and ('recipe' in full_p_file) ):
                       print 'Analyzing:', full_p_file
                       file2read = open(full_p_file, 'rU')
                       fileAsStr = file2read.read()
                       if full_p_file not in dict2dump:
                          dict2dump[full_p_file] = fileAsStr

    pickle.dump(dict2dump, open('CHEF_CONTENT_PICKLE.pickle', 'wb'))
    dump_status=os.stat('CHEF_CONTENT_PICKLE.pickle').st_size
    print 'DUMPED A CHEF PICKLE FILE OF {} BYTES'.format(dump_status)

def getScriptID(id_, dict_, name_):
     all_ids = dict_[name_]
     # print all_ids
     list_len = len(all_ids)
     if id_ < list_len :
        scriptID = all_ids[id_]
     else:
        scriptID = all_ids[random.randrange(0, list_len)]
     return scriptID

def getIDBData(IBD_File_P, all_id_dict):
        idbDict = {}
        with open(IBD_File_P, 'rU') as file_:
             reader_ = csv.reader(file_)
             next(reader_, None)
             for row_ in reader_:
                 stdID = row_[0]

                 MOZ_ID = row_[1].split('L')[1]
                 moz_script_id = getScriptID(MOZ_ID, all_id_dict, 'MOZ')

                 OST_ID = row_[2].split('L')[1]
                 ost_script_id = getScriptID(OST_ID, all_id_dict, 'OST')

                 WIK_ID = row_[3].split('L')[1]
                 wik_script_id = getScriptID(WIK_ID, all_id_dict, 'WIK')

                 BLO_ID = row_[4].split('L')[1]
                 blo_script_id = getScriptID(BLO_ID, all_id_dict, 'BERG')

                 CAS_ID = row_[5].split('L')[1]
                 cas_script_id = getScriptID(CAS_ID, all_id_dict, 'CASK')

                 EXP_ID = row_[6].split('L')[1]
                 exp_script_id = getScriptID(EXP_ID, all_id_dict, 'EXPR')

                 if stdID not in idbDict:
                     idbDict[stdID] = [(stdID, moz_script_id), (stdID, ost_script_id), (stdID, wik_script_id),
                                       (stdID, blo_script_id), (stdID, cas_script_id), (stdID, exp_script_id)]
                 else:
                     idbDict[stdID] = idbDict[stdID] + [(stdID, moz_script_id), (stdID, ost_script_id), (stdID, wik_script_id),
                                       (stdID, blo_script_id), (stdID, cas_script_id), (stdID, exp_script_id)]

        return idbDict


def makeAssi(ID_File, IBD_File):
        allIDDict = {}
        with open(ID_File, 'rU') as file_:
             reader_ = csv.reader(file_)
             for row_ in reader_:
                 org_of_file = row_[2]
                 id_of_file  = row_[0]
                 if org_of_file not in allIDDict:
                     allIDDict[org_of_file] = [id_of_file]
                 else:
                     allIDDict[org_of_file] = allIDDict[org_of_file] + [id_of_file]
        idbDict = getIDBData(IBD_File, allIDDict)
        str2write = ''
        for std, assi in idbDict.iteritems():
            cnt_ = 0
            for in_ in xrange(len(assi)):
                cnt_ = in_ + 1
                str2write = str2write + assi[in_][1] + ',' + assi[in_][0] + ','  + str(cnt_) + '\n'
        print str2write

def createAssiFile(file_name):
    str2write  = ''
    with open(file_name, 'rU') as file_:
         reader_ = csv.reader(file_)
         for row_ in reader_:
             id_of_file  = row_[0]
             id_of_stud  = row_[1]
             realStdID   = id_of_stud.split('_')[0] + id_of_stud.split('_')[1]
             id_of_cnt   = row_[2]
             str2write   = str2write + id_of_file + ',' + realStdID + ',' + id_of_cnt  + '\n'
    print str2write

if __name__=='__main__':
    # ds_paths = ['/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_BASTION_FULL_PROCESS_DATASET.csv',
    #             '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_CISCO_FULL_PROCESS_DATASET.csv',
    #             '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_MIRANTIS_FULL_PROCESS_DATASET.csv',
    #             '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_MOZ_FULL_PROCESS_DATASET.csv',
    #             '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_OPENSTACK_PROCESS_DATASET.csv',
    #             '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_WIKI_FULL_PROCESS_DATASET.csv']
    # #####createPickle(ds_paths)  ### WILL NOT BE CALLED AS PICKLE FILE GENRATED
    # insertAllData('ALL_CONTENT_PICKLE.pickle')

    # all_chef_list = ['/Users/akond/SECU_REPOS/berg-chef/chef-bcpc-2016-12/',
    #                  '/Users/akond/SECU_REPOS/cdat-chef/cdap_cookbook-2016-12/',
    #                  '/Users/akond/SECU_REPOS/cdat-chef/hadoop_cookbook-2016-12/',
    #                  '/Users/akond/SECU_REPOS/cdat-chef/impala_cookbook-2016-12/',
    #                  '/Users/akond/SECU_REPOS/expr-chef/consul_lwrp-2016-12/',
    #                  '/Users/akond/SECU_REPOS/expr-chef/openvpn-2016-12/',
    #                  '/Users/akond/SECU_REPOS/expr-chef/postgresql_lwrp-2016-12/',
    #                  '/Users/akond/SECU_REPOS/expr-chef/zabbix_lwrp-2016-12/'
    #                  ]
    # insertChefData(all_chef_list)

    # '''
    # function to create assignments
    # '''
    # scriptIDFile = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/ALL_SCRIPT_ID.csv'
    # IBDFile = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/IBD_DATA.csv'
    # makeAssi(scriptIDFile, IBDFile)

    # SemiAssiFile = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/ALL_ASS.csv'
    # createAssiFile(SemiAssiFile)

    '''
    generate tokens for students 
    '''
