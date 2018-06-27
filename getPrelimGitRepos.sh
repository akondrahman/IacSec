#!/bin/bash 
echo "### This script extracts puppet related repsoitoiries from the internet###"
cnt_repo=0
while IFS='' read -r line || [[ -n "$line" ]]; do
   echo " "  
   repo_name=$line
   git clone $repo_name 
   echo "Cloning done ... looking at count of puppet files in"$repo_name  
   cnt=`find $repo_name  -type f -name '*.pp' | wc -l`
   echo "Number fo puppet files in this repo:"$cnt 
  if [ "$cnt" -gt 0 ]; then ## always quote your avriables
    cnt_repo=$((cnt_repo + 1))  
    echo "This repository has puppet files. Keeping:"$repo_name
  else
    echo "This repository has no puppet files. Deleting:"$repo_name
    rm -rf $repo_name 
  fi
  echo "---------------------------"     
  echo " "     
done < "$1"         
echo "In total we have downloaded $cnt_repo repositoires. Yeeay!"