'''
Akond Rahman 
Apr 27, 2019 
Get curated dataset for Ansible and Chef 
'''
import pandas as pd 
import numpy as np 

def getDF(ap_df_, sub_df_, script_df_, ext_):
    script_dict = {}
    full_file_list = list(np.unique(sub_df_['ScriptID'].tolist()) )
    # print full_file_list
    for scriptID in full_file_list:
        script_as_list  = script_df_[script_df_['ScriptID']==scriptID]['path'].tolist()
        if(len(script_as_list)) > 0:
            script = script_as_list[0]
            if ext_ in script:
                script_ap_ID   = sub_df_[sub_df_['ScriptID']==scriptID]['APID'].tolist()[0]
                script_ap_name = ap_df_[ap_df_['APID']==script_ap_ID]['Name'].tolist()[0]
                # print script_ap_ID, script_ap_name 
                
                if script not in script_dict:
                    script_dict[script] = [script_ap_name]
                else:
                    script_dict[script] = script_dict[script] + [script_ap_name]
    agree_count, disagree_count = 0, 0 
    agree_list, disagree_list = [], []
    # print script_dict
    for script, categs in script_dict.iteritems():
        if len(np.unique(categs)) > 1:
            disagree_count = disagree_count + 1 
            disagree_list.append((script, 'DISAGREED', 'TBD'))
        else: 
            agree_count = agree_count + 1 
            agree_list.append((script, 'AGREED', list(np.unique(categs))[0])) 
    agree_df    = pd.DataFrame(agree_list) 
    disagree_df = pd.DataFrame(disagree_list)
    return agree_count, disagree_count, agree_df, disagree_df 


if __name__=='__main__':
    anti_pattern_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/closed-coding-2019/ap2019.csv'
    script_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/closed-coding-2019/script2019.csv'
    submission_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/closed-coding-2019/submission2019.csv' 

    chef_final_file_agr = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED_CHEF_AGREE.csv'
    chef_final_file_dis = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED_CHEF_DISAGREE.csv'

    ansi_final_file1 = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED_ANSI_1.csv'
    ansi_final_file2 = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/COMPLETE_CURATED_ANSI_2.csv'

    ap_df  = pd.read_csv(anti_pattern_file)
    sub_df = pd.read_csv(submission_file)
    scr_df = pd.read_csv(script_file) 

    # print ap_df.head() 
    # print ' '
    # print sub_df.head() 
    # print ' '
    # print scr_df.head() 
    # print ' '        

    '''
    DO NOT UNCOMMENT line# 65 -71 
    '''

    # yml_agreements, yml_disagreemnts, yml_agree_df, yml_disagree_df = getDF(ap_df, sub_df, scr_df, 'yml') 
    # yml_agree_df.to_csv(ansi_final_file1)
    # print '.yml', yml_agreements, yml_disagreemnts 

    # yaml_agreements, yaml_disagreemnts, yaml_agree_df, yaml_disagree_df = getDF(ap_df, sub_df, scr_df, 'yaml') 
    # yaml_agree_df.to_csv(ansi_final_file2) 
    # print '.yaml', yaml_agreements, yaml_disagreemnts     

    # chef_agreements, chef_disagreemnts, chef_agree_df, chef_disagree_df = getDF(ap_df, sub_df, scr_df, 'rb') 
    # chef_agree_df.to_csv(chef_final_file_agr)  
    # chef_disagree_df.to_csv(chef_final_file_dis)
    # print '.rb', chef_agreements, chef_disagreemnts     
