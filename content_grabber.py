'''
Akond Rahman
Nov 08, 2017
Content grabber for S&P project
Wednesday
'''

import utility

bastion_file   = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_BASTION_FULL_DATASET.csv'
cisco_file     = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_CISCO_FULL_DATASET.csv'
mirantis_file  = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_MIRANTIS_FULL_DATASET.csv'
mozilla_file   = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_MOZ_FULL_DATASET.csv'
openstack_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_OST_FULL_DATASET.csv'
wikimedia_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/PHASE7_WIKI_FULL_DATASET.csv'




if __name__=='__main__':
    bastion_files   = utility.getFileFromCSV(bastion_file)
    cisco_files     = utility.getFileFromCSV(cisco_file)
    mirantis_files  = utility.getFileFromCSV(mirantis_file)
    mozilla_files   = utility.getFileFromCSV(mozilla_file)
    openstack_files = utility.getFileFromCSV(openstack_file)
    wikimedia_files = utility.getFileFromCSV(wikimedia_file)

    file_counter = 0
    list_of_ds = [bastion_files,  cisco_files, mirantis_files, mozilla_files , openstack_files, wikimedia_files]
    for ds_ in list_of_ds:
        for file_content in ds_:
            file_counter += 1
            print '='*25 + str(file_counter) + 'START!' + '='*25
            print file_content
            print '='*25 + str(file_counter) + 'END!!!' + '='*25
