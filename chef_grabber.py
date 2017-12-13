'''
Akond Rahman
Dec 12, 2017
Tuesday
Content grabber for Chef scripts
'''
import os
def getAllChefScripts(root_path):
    valid_file = 0
    for root, subFolders, files in os.walk(root_path):
        for file_obj in files:
            if file_obj.endswith('.rb'):
               file2read = os.path.join(root, file_obj)
               #check if file path includes valid sub directories: 'attributes', 'definitions', 'libraries', 'recipes'
               #another option is ot detect only 'recipes', will decide later
               # if('recipes' in file2read):
               if(('attributes' in file2read) or ('definitions' in file2read) or ('libraries' in file2read) or ('recipes' in file2read)):
                  valid_file += 1
                  print 'Extracting:', file2read
                  if(os.path.exists(file2read)):
                     with open(file2read, 'rU') as the_file:
                         content_full = the_file.read()
                         print '='*25 + ':'*3 + str(valid_file)   + ':'*3  + 'START!' + '='*25
                         print content_full
                         print '*'*10
                         print 'DECISION===>:'
                         print '*'*10
                         print '='*25 + ':'*3   + str(valid_file) + ':'*3  + 'END!!!' + '='*25
        # print root

def getValidRepos(file_):
    all_repo_list = []
    with open(file_, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
          repo_name = row_[0]
          all_repo_list.append(repo_name)
    return all_repo_list

if __name__=='__main__':
    root_dir = '/Users/akond/CHEF_REPOS/github-downloads/'
    valid_repos=getValidRepos(root_dir + 'eligible_repos.csv')
    print 'Total valid repos:', len(valid_repos)
    getAllChefScripts(valid_repos)
