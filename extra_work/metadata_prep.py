'''
Need a short list to get the meta data 
Akond Rahman
July 02, 2018 
'''
import csv 
import os 

def getAllNames(the_file):
    all_repos = []
    with open(the_file, 'rU') as log_fil:
         file_str = log_fil.read()
         all_repos = file_str.split('\n')
    all_repos = [x_ for x_ in all_repos if len(x_) > 0]
    return all_repos

def getFilteredNames(in_):
    filtered_repos = []
    with open(in_, 'rU') as file_:
      reader_ = csv.reader(file_)
      for row_ in reader_:
          name_ = row_[0]
          filtered_repos.append(name_)
    return filtered_repos

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP )
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

if __name__=='__main__':
   filtered_list_file = 'v3_filtered_list.csv'
   all_list_file = 'all_pp_repo_names.txt'
   filt_list = getFilteredNames(filtered_list_file)
   all_list = getAllNames(all_list_file)
   list_to_explore = []
   for name_ in all_list:
       for filtered_name in filt_list:
           if (name_.split('/')[-1]==filtered_name) :
              list_to_explore.append(name_)
   str_to_dump = '' 
   list_to_explore = np.unique(list_to_explore)
   for repo_name in list_to_explore:
       str_to_dump = str_to_dump + repo_name + '\n'
   dumpContentIntoFile(str_to_dump, 'RepoListForMetaData.txt')