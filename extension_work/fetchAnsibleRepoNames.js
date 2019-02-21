// code to get Ansible repo names 
// need to run in msr19/source for dependencies 
const BigQuery = require('@google-cloud/bigquery');
var fs = require('fs');

const projectId = "githubsolidityquery";
const sqlQuery = 'SELECT * FROM `LOL.TSE_ANSIBLE_GITHUB_REPOS`' ; 

var out_fil = 'TSE_GITHUB_ANSIBLE_REPO_NAMES.csv'

const bigquery = new BigQuery({
  projectId: projectId,
  keyFilename: '', 
  location: 'US'
});

const options = {
  query: sqlQuery,
  useLegacySql: false, 
};

let job;
var fullData = '' ;


bigquery
  .createQueryJob(options)
  .then(results => {
    job = results[0];
    console.log(`Job ${job.id} started.`);
    return job.promise();
  })
  .then(() => {
    return job.getMetadata();
  })
  .then(metadata => {
    const errors = metadata[0].status.errors;
    if (errors && errors.length > 0) {
      throw errors;
    }
  })
  .then(() => {
    console.log(`Job ${job.id} completed.`);
    return job.getQueryResults();
  })
  .then(results => {
    const rows = results[0];
    rows.forEach(function(row_as_json){
      owner_name  = row_as_json['owner'];
      repo_name   = row_as_json['repo_name'];
      repo_link   = 'https://github.com/' + owner_name + '/' + repo_name 
      
      data   = owner_name + ',' + repo_name + ',' + repo_link + ',' + '\n' ;
      fullData = fullData + data ; 
    });

    fs.writeFile(out_fil, fullData, function(err) {
    if(err) {
        return console.log(err);
    }
        console.log("Ansible Github repo names dumped succesfully ... ");
    }); 

  })
  .catch(err => {
    console.error('ERROR:', err);
  });