'''
Utility file for secuirty and privacy porject
Akond Rahman
Nov 08, 2017
Wednesday
'''
import csv
import os
import os.path


def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)


def getFileFromCSV(the_ds_file):
    all_file_content = []
    with open(the_ds_file, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        full_path_of_file  = row_[1]  # the file name from dataset
        if(os.path.exists(full_path_of_file)):
           with open(full_path_of_file, 'rU') as the_file:
             content_full = the_file.read()
             all_file_content.append((content_full, full_path_of_file))   ### each file conent is now one big string
    return all_file_content
