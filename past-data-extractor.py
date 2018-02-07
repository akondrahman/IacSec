'''
Akond Rahman
Feb 07, 2018
Script to extract time wise data extract
'''
import os


def generatePastData(folder_path, y_p, m_p):
    all_dirs = [x[0] for x in os.walk(folder_path)]
    for dir_ in all_dirs:
        for year_ in y_p:
            for mont_ in m_p:
                folder2create = dir_ + '/' + year_ + '-' + mont_
                print folder2create

if __name__=='__main__':
   folder2walk = '/Users/akond/SECU_REPOS/test-pup/'
   y_list = ['2011', '2012', '2013', '2014', '2015', '2016']
   m_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

   generatePastData(folder2walk, y_list, m_list)
