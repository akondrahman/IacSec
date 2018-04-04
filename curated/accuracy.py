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


if __name__=='__main__':
   curated_ds = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/datasets/curated/Test.csv'
   printAccu(curated_ds)
