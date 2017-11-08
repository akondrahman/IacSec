'''
Utility file for secuirty and privacy porject
Akond Rahman
Nov 08, 2017
Wednesday
'''

import os



def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP)
    fileToWrite.close()
    return str(os.stat(fileP).st_size)


def getPuppetFileDetails(the_ds_file):
    all_file_content = []
    with open(the_ds_file, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        full_path_of_file  = row_[1]
        with open(full_path_of_file, 'rU') as the_file:
             content_full = the_file.read()
             all_file_content.append(content_full)
    return all_file_content         
