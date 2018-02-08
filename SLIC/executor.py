'''
Akond Rahman
Feb 08, 2018
Executor : detects the script type, and triggers the linter
'''
import os

def sniffSmells(path_to_dir):
    for root, dirs, files in os.walk(path_to_dir):
       for file_ in files:
           if file_.endswith(".pp"):
             print "Started analyzing:", os.path.join(root, file_)
             print "="*50
