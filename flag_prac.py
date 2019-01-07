'''
Command line flag practice 
Dhaka
Akond Rahman 
'''
import sys 
import getopt


if __name__=='__main__': 
   try:
      arglis = sys.argv[1:] 
   except:
      print 'Correct command: `python main.py <FLAG>` ' 
      print 'Available flags are: `-h`, `-g`, `-m`, `-o`, and `-w` '  
      sys.exit(2)
   for opt in arglis:
      if opt == '-h':
        print 'You have reached the helpline'
        print 'Correct command: `python main.py <FLAG>` ' 
        print 'Available flags are: `-g`, `-h`, `-m`, `-o`, and `-w` '  
        sys.exit(2)
      elif opt == '-g':
        ds_path = '/Users/akond/SECU_REPOS/ghub-pupp/'
        output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_GITHUB_PUPPET.csv'
        sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_GIT_PUP.PKL'
      elif opt == '-m':
        ds_path = '/Users/akond/SECU_REPOS/mozi-pupp/'
        output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_MOZILLA_PUPPET.csv'
        sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_MOZ_PUP.PKL'
      elif opt == '-o':
        ds_path = '/Users/akond/SECU_REPOS/ostk-pupp/'
        output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_OPENSTACK_PUPPET.csv'
        sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_OST_PUP.PKL'
      elif opt == '-w':
        ds_path = '/Users/akond/SECU_REPOS/wiki-pupp/'
        output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_ALL_WIKIMEDIA_PUPPET.csv'
        sym_output_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/V10_SYM_ALL_WIK_PUP.PKL'
      else: 
        print 'Correct command is `python main.py` <FLAG>' 
        print 'Available flags are: `-h`, `-g`, `-m`, `-o`, and `-w` '  

   print 'Dataset path:', ds_path
   print 'Output file path:', output_file 
   print 'Symbolic file path:', sym_output_file