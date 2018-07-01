#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
  repo_name=$line
  echo "----------------------------------------------------------------------------"
  echo $repo_name
  jsonFileName=`echo $repo_name | tr '/' _`
  # echo $jsonFileName
  curl -H "Authorization: token <TOKEN_GOES_HERE>" -ni "https://api.github.com/repos/"$repo_name -H 'Accept: json' > $jsonFileName.json
  echo "----------------------------------------------------------------------------"
done < "$1" 
