'''
Script to add values to database table
Akond Rahman
Nov 23, 2017
Thursday, thanksgiving day
'''
import pymysql.cursors
import cPickle as pickle
import os, csv

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


if __name__=='__main__':
    ds_paths = ['/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_BASTION_FULL_PROCESS_DATASET.csv',
                '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_CISCO_FULL_PROCESS_DATASET.csv',
                '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/OCT17_MIRANTIS_FULL_PROCESS_DATASET.csv',
                '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_MOZ_FULL_PROCESS_DATASET.csv',
                '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_OPENSTACK_PROCESS_DATASET.csv',
                '/Users/akond/Documents/AkondOneDrive/OneDrive/ProcessInIaC/dataset/MultiTasking_WIKI_FULL_PROCESS_DATASET.csv']
    #####createPickle(ds_paths)  ### WILL NOT BE CALLED AS PICKLE FILE GENRATED
    insertAllData('ALL_CONTENT_PICKLE.pickle')
