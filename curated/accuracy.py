'''
April 03, 2018
Tuesday
Akond Rahman
Script to detect accuracy of SLIC
'''

from sklearn.metrics import precision_score, recall_score
import numpy as np, pandas as pd
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def printAccu(file_name):
  df2read = pd.read_csv(file_name)
  actualLabels = df2read['ACTUAL'].tolist()
  predictedLabels = df2read['TOOL'].tolist()
  # print actualLabels
  '''
    the way skelarn treats is the following: first index -> lower index -> 0 -> 0
                                             next index after first  -> next lower index -> 1 -> 1
  '''
  col_nam = ['HARD_CODE_SECR', 'SUSP_COMM', 'SECR_LOCA', 'MD5_USAG', 'HTTP_USAG',	'BIND_USAG', 'EMPT_PASS',
           'DFLT_ADMN',	'BASE_64',	'MISS_DFLT', 'TOTAL', 'NONE']
  '''
  getting the confusion matrix
  '''
  print "Confusion matrix start"
  #print conf_matr_output
  conf_matr_output = confusion_matrix(actualLabels, predictedLabels)
  print conf_matr_output
  print "Confusion matrix end"
  print ">"*10
  '''
  '''
  print "precison, recall, F-stat"
  class_report = classification_report(actualLabels, predictedLabels)
  print class_report
  print ">"*10
  '''
  accuracy_score ... reff: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter .... percentage of correct predictions
  ideally 1.0, higher the better
  '''
  accuracy_score_output = accuracy_score(actualLabels, predictedLabels)
  # preserve the order first test(real values from dataset), then predcited (from the classifier )
  print "Accuracy output is ", accuracy_score_output
  print">"*10

def getLabels(file_):
    df_ = pd.read_csv(file_)
    ls_ = []
    col_nam = ['HARD_CODE_SECR', 'SUSP_COMM', 'SECR_LOCA', 'MD5_USAG', 'HTTP_USAG',	'BIND_USAG', 'EMPT_PASS',
               'DFLT_ADMN',	'BASE_64',	'MISS_DFLT', 'TOTAL']
    for col_ in col_nam:
        df_sel_fil_lis = df_[df_[col_]>0]['FILE_NAME'].tolist()
        for fil_itm in df_sel_fil_lis:
            ls_.append((fil_itm, col_, col_))
    # to handle category 'none'
    none_fil_lis = df_[df_['TOTAL']==0]['FILE_NAME'].tolist()
    for non_fil_itm in none_fil_lis:
            ls_.append((fil_itm, 'NONE', 'NONE'))

    return ls_

def createDS(agr_fil, dis_agr_fil):
    agr_ls = getLabels(agr_fil)
    dis_agr_ls = getLabels(dis_agr_fil)
    complete_ls = agr_ls + dis_agr_ls
    df2ret = pd.DataFrame([x for x in complete_ls], columns=['SCRIPT', 'ACTUAL', 'TOOL'])
    return df2ret

if __name__=='__main__':
   '''
   Step-1 : create the dataset from agree and disagree file
   '''
   # agree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/AGREE_CHEF.csv'
   # disagree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/DISAGREE_CHEF.csv'

   # agree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/AGREE_ANSI.csv'
   # disagree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/DISAGREE_ANSI.csv'

   # curated_df = createDS(agree_file, disagree_file)
   # need to dump csv for hacking, after dumping check CSV, make chnages if needed , and save it as final
   # curated_df.to_csv('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/V6_SEMIFINAL.csv')
   '''
   Step-2 : pass the dataset to get accuracy
   '''
   #curated_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/V10_FINAL.csv'

   '''
   Step-3 : sanity dataset to get accuracy
   '''
   sanity_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/sanity-check/V3_SANITY.csv'

   printAccu(sanity_ds)
