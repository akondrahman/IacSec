'''
Akond Rahman
Dec 12, 2017
Tuesday
Content grabber for Chef scripts
'''
import os
def getAllChefScripts(root_path):
    for root, subFolders, files in os.walk(root_path):
        for file_obj in files:
            print file_obj

if __name__=='__main__':
    root_dir = '/Users/akond/CHEF_REPOS/github-downloads/'
    getAllChefScripts(root_dir)
