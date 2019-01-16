The artifact is a Docker image which contains source code for Security Linter for Infrastructure as Code (SLIC). SLIC 
is a static analysis tool that looks for security smells in infrastructure as code (IaC) scripts. The Docker image also includes the directories where 
we have Puppet scripts for which we run SLIC and perform empirical analysis. The easiest way to run SLIC is to execute instructions 1-8 mentioned below.  

The seven security smells are listed in our ICSE 2019 paper 'The Seven Sins: Security Smells in Infrastructure as Code'. The pre-print of the paper 
is available here: https://akondrahman.github.io/papers/icse19_slic.pdf 


The artifact is available here: https://cloud.docker.com/repository/docker/akondrahman/ruby_for_sp/general 

Dependencies: Docker 

Instructions to replicate: 


1. Install Docker on your computer 
2. Go to terminal 
3. run the command `docker pull akondrahman/ruby_for_sp`
4. run the command `docker run -it --name slic akondrahman/ruby_for_sp bash` 
5. run the command `cd /SecurityInIaC/IacSec/SLIC/`


> To get the results for a few test scripts it takes *0.04 minutes to complete*. run `python main.py -t`. This command will execute SLIC for the test scripts. Upon completion of the analysis `Dumped CSV output file of 1197 bytes`, `Dumped symbolic output PICKLE of 6 bytes`, and `Duration: 0.0453675349553 minutes` will be displayed, which indicates that SLIC's execution is complete. 


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



Abstract: 

Paper title: *The Seven Sins: Security Smells in Infrastructure as Code Scripts* 

_Practitioners use infrastructure as code (IaC) scripts to provision servers and development environments. While developing IaC scripts, practitioners may inadvertently introduce security smells. Security smells are recurring coding patterns that are indicative of security weakness and can potentially lead to security breaches. The goal of sharing the research artifact is to help software practitioners and researchers use our static analysis tool Security Linter for Infrastructure as Code (SLIC) to identify security smells in infrastructure as code scripts.  We are applying for the Available badge. We provide a Docker-based research artifact to use and replicate the major findings presented in the paper. The artifact is a Docker image which contains source code for SLIC. The Docker image also includes the directories where we have Puppet scripts for which we run SLIC and perform empirical analysis. To run our tool it is required to have Docker installed. Basic skills in Docker is sufficient such as 'docker pull' and 'docker run'. We have provided detailed instructions on installations and how to run the tool in README.md and INSTALL.md. DOI for the tool: https://doi.org/10.6084/m9.figshare.6943316_ 