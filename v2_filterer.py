'''
Akond Rahman 
June 30, 2018 
Get commit count and month diffs 
'''
import os 
import csv 
from datetime import date

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP )
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

def getMonDiff(st_mo, en_mo):
    d0 = date(int(st_mo.split('-')[0]), int(st_mo.split('-')[1]), int(st_mo.split('-')[2]))
    d1 = date(int(en_mo.split('-')[0]), int(en_mo.split('-')[1]), int(en_mo.split('-')[2]))
    delta = d1 - d0
    mon_ =  float(delta.days) / float(30)
    if mon_ <= 1.0 :
        mon_ = 1.0
    return mon_

def findValidRepos(file_p):
    valid_list = []
    with open(file_p, 'rU') as file_:
        reader_ = csv.reader(file_)
        for row_ in reader_:
            repo_name    = row_[0]    
            start_month  = row_[1]    
            end_month    = row_[2]
            commit_count = int(row_[3])

            months = getMonDiff(start_month, end_month)                        
            comm_per_mon = float(commit_count)/float(months)
            print repo_name, months 
            if comm_per_mon >= 2.0  :
                valid_list.append(repo_name)
    str_ = ''
    for repo_ in valid_list:
        str_ = str_ + repo_ + ',' + '\n'
        
    return str_
                

if __name__=='__main__':
   the_file = '/Users/akond.rahman/Documents/Personal/IacSec/extra_work/v2_filtered_at_least_two.csv'
   out_fil = '/Users/akond.rahman/Documents/Personal/IacSec/extra_work/v3_filtered_list.csv' 
   str_dump = findValidRepos(the_file)
   dumpContentIntoFile(str_dump, out_fil)
