The tool comes as a Docker image. Steps to execute the tool:

Dependencies: Docker 

Instructions to replicate: 


1. Install Docker on your computer 
2. Go to terminal 
3. run the command `docker pull akondrahman/ruby_for_sp`
4. run the command `docker run -it --name slic akondrahman/ruby_for_sp bash` 


This will get the tool running on terminal 

Instructions to run tool and see results: 


1. Install Docker on your computer 
2. Go to terminal 
3. run the command `docker pull akondrahman/ruby_for_sp`
4. run the command `docker run -it --name slic akondrahman/ruby_for_sp bash` 
5. run the command `cd /SecurityInIaC/IacSec/SLIC/`


> To get the results for the Mozilla repositories it takes *251 minutes to complete*. Follow steps 6-8: 
6. run `python main.py -m`. This command will execute SLIC for the scripts collected from the Mozilla repositories. Upon completion of the analysis `Dumped CSV output file of XXX bytes`, `Dumped symbolic output PICKLE of XXX bytes`, and `Ended at:XXX` will be displayed, which indicates that SLIC's execution is complete and it generated the result files used to answer RQ2 and RQ3. 
7. run `cd /SecurityInIaC/IacSec/analysis/`
8. run `python frq_cnt.py -m`. Upon execution the results of RQ2 will be obtained. Compare obtained results with the results presented in Table VIII of the paper. The results that correspond to the month 2018-06, correspond to the results presented in the paper.  


> To get the results for the Openstack repositories it takes *725 minutes to complete*. Follow steps 6-8:
6. run `python main.py -o`. This command will execute SLIC for the scripts collected from the Openstack repositories. Upon completion of the analysis `Dumped CSV output file of XXX bytes`, `Dumped symbolic output PICKLE of XXX bytes`, and `Ended at:XXX` will be displayed, which indicates that SLIC's execution is complete and it generated the result files used to answer RQ2 and RQ3. 
7. run `cd /SecurityInIaC/IacSec/analysis/`
8. run `python frq_cnt.py -o`. Upon execution the results of RQ2 will be obtained. Compare obtained results with the results presented in Table VIII of the paper. The results that correspond to the month 2018-06, correspond to the results presented in the paper.  


> To get the results for the Wikimedia repositories it takes *286 minutes to complete*. Follow steps 6-8: 
6. run `python main.py -w`. This command will execute SLIC for the scripts collected from the Wikimedia repositories. Upon completion of the analysis `Dumped CSV output file of XXX bytes`, `Dumped symbolic output PICKLE of XXX bytes`, and `Ended at:XXX` will be displayed, which indicates that SLIC's execution is complete and it generated the result files used to answer RQ2 and RQ3. 
7. run `cd /SecurityInIaC/IacSec/analysis/`
8. run `python frq_cnt.py -w`. Upon execution the results of RQ2 will be obtained. Compare obtained results with the results presented in Table VIII of the paper. The results that correspond to the month 2018-06, correspond to the results presented in the paper.  

> To get the results for the GitHub repositories it takes *1431.9 minutes to complete*. Follow steps 6-8:
6. run `python main.py -g`. This command will execute SLIC for the scripts collected from the GitHub repositories. Upon completion of the analysis `Dumped CSV output file of XXX bytes`, `Dumped symbolic output PICKLE of XXX bytes`, and `Ended at:XXX` will be displayed, which indicates that SLIC's execution is complete and it generated the result files used to answer RQ2 and RQ3. 
7. run `cd /SecurityInIaC/IacSec/analysis/`
8. run `python frq_cnt.py -g`. Upon execution the results of RQ2 will be obtained. Compare obtained results with the results presented in Table VIII of the paper. The results that correspond to the month 2018-06, correspond to the results presented in the paper.  
