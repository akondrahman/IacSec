'''
Akond Rahman
Dec 12, 2017
Tuesday
Content grabber for Chef scripts
'''
import os
import csv
def getAllChefScripts(repo_list, root_path, repo_25_path):
    valid_file = 0
    for repo_ in repo_list:
       if repo_ in repo_25_path:
          path2look = root_path + repo_
          for root, subFolders, files in os.walk(path2look):
             for file_obj in files:
               if file_obj.endswith('.rb'):
                  file2read = os.path.join(root, file_obj)
                  #check if file path includes valid sub directories: 'attributes', 'definitions', 'libraries', 'recipes'
                  #another option is ot detect only 'recipes', will decide later
                  if('recipes' in file2read):
                  # if(('attributes' in file2read) or ('definitions' in file2read) or ('libraries' in file2read) or ('recipes' in file2read)):
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

def getStarredRepos(file_):
    all_repo_list = [line.rstrip('\n') for line in open(file_)]
    all_repo_list = [x_.split('/')[-1] for x_ in all_repo_list]
    return all_repo_list

if __name__=='__main__':
    # root_dir = '/Users/akond/CHEF_REPOS/github-downloads/'
    # valid_repos=getValidRepos(root_dir + 'eligible_repos.csv')
    # repo_25stars=getStarredRepos(root_dir + 'repo_25stars.txt')
    # print 'Total valid repos:', len(valid_repos)
    # print '-'*100
    # getAllChefScripts(valid_repos, root_dir, repo_25stars)

    root_dir = '/Users/akond/CHEF_REPOS/github-downloads/valid_100_repos/'
    valid_repos=getValidRepos(root_dir + 'final_eligible_repos.csv')
    repo_100stars=getStarredRepos(root_dir + 'valid_100star_repos.txt')
    print 'Total valid repos:', len(valid_repos)
    print '-'*100
    getAllChefScripts(valid_repos, root_dir, repo_100stars)
