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
  target_labels =  [0, 1, 2]
  '''
  getting the confusion matrix
  '''
  print "Confusion matrix start"
  #print conf_matr_output
  conf_matr_output = confusion_matrix(actualLabels, predictedLabels, labels=target_labels)
  print conf_matr_output
  print "Confusion matrix end"
  print ">"*10
  '''
  '''
  print "precison, recall, F-stat"
  class_report = classification_report(actualLabels, predictedLabels, labels=target_labels)
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
            ls_.append((fil_itm, col_, col_))
    df2ret = pd.DataFrame([x for x in ls_], columns=['SCRIPT', 'ACTUAL', 'PREDICTED'])
    return df2ret

def createDS(agr_fil, dis_agr_fil):
    agr_df = getLabels(agr_fil)
    dis_agr_df = getLabels(dis_agr_fil)
    print agr_df.head()
    print dis_agr_df.head()

if __name__=='__main__':
   '''
   Step-1 : create the dataset from agree and disagree file
   '''
   agree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/V6_CURATED_AGREE_PUPPET.csv'
   disagree_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/curated/V6_CURATED_DISAGREE_PUPPET.csv'
   createDS(agree_file, disagree_file)
   '''
   Step-2 : pass the dataset to get accuracy
   '''
   # curated_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/Test.csv'
   # printAccu(curated_ds)
