'''
Akond Rahman 
Jan 30, 2020 
Get data for PROMISE 
'''
import numpy as np 
import pandas as pd 


def mergeDataFrame(raw_df, valid_df, output_file): 
    full_data       = [] 
    already_visited = []

    valid_df  = valid_df[valid_df['TYPE'] != 'SECURITY:::HARD_CODED_SECRET_USER_NAME:::']
    valid_df  = valid_df[valid_df['TYPE'] != 'SECURITY:::HARD_CODED_SECRET_PASSWORD:::']
    valid_df  = valid_df[valid_df['TYPE'] != 'SECURITY:::BASE64:::']
    # print(np.unique(valid_df['TYPE'].tolist())) 


    TP_DF     = valid_df[valid_df['VALID']==1]
    TP_FILES  = np.unique(  TP_DF['FILEPATH'].tolist() )
    FP_DF     = valid_df[valid_df['VALID']==0] 
    FP_FILES  = np.unique(  FP_DF['FILEPATH'].tolist() ) 

    for file_ in TP_FILES: 
        if file_ not in already_visited:
            file_df = valid_df[valid_df['FILEPATH']==file_]
            types   = file_df['TYPE'].tolist() 
            for type_ in types: 
                tup_ = (file_, type_)
                full_data.append(tup_) 

    for file_ in FP_FILES: 
        if file_ not in already_visited:
            tup_ = (file_, 'NONE') 
            full_data.append(tup_) 

    ALL_FILES = raw_df['FILE_NAME'].tolist() 
    for file_ in ALL_FILES: 
        if file_ not in already_visited:
            tup_ = (file_, 'NONE') 
            full_data.append(tup_) 
    final_df = pd.DataFrame(full_data) 
    final_df.to_csv(output_file, header=['FILENAME', 'ICP_TYPE' ], index=False, encoding='utf-8')    
    print(len(np.unique( pd.read_csv(output_file)['FILENAME'].tolist() )))



if __name__=='__main__':
    # RAW_DATASET_FILE   = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/RAW_DATASETS/V2_ALL_MOZILLA_PUPPET.csv'
    # VALID_MAPPING_FILE = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/FILTERED_MOZILLA_COLOCATION.csv'
    # FINAL_OUTPUT_FILE  = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/LOCKED_MOZILLA_COLOCATION.csv'

    # RAW_DATASET_FILE   = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/RAW_DATASETS/V2_ALL_OPENSTACK_PUPPET.csv'
    # VALID_MAPPING_FILE = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/FILTERED_OPENSTACK_COLOCATION.csv'
    # FINAL_OUTPUT_FILE  = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/LOCKED_OPENSTACK_COLOCATION.csv'

    # RAW_DATASET_FILE   = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/RAW_DATASETS/V2_ALL_WIKIMEDIA_PUPPET.csv'
    # VALID_MAPPING_FILE = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/FILTERED_WIKIPEDIA_COLOCATION.csv'
    # FINAL_OUTPUT_FILE  = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/IaC/ICP_Localization/FILTERED_DATASETS/LOCKED_WIKIPEDIA_COLOCATION.csv'

    RAW_DATAFRAME   = pd.read_csv(RAW_DATASET_FILE)
    VALID_DATAFRAME = pd.read_csv(VALID_MAPPING_FILE)    

    mergeDataFrame(RAW_DATAFRAME, VALID_DATAFRAME, FINAL_OUTPUT_FILE)   
