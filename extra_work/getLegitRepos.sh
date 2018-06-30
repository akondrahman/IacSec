#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
  repo_name=$line
  # echo $repo_name
  ## get into the repo name
  cd $repo_name
  latest_commit_date=`git log -1 --date=short --pretty=format:%cd`
  # echo "Latest commit date:"
  # echo $latest_commit_date
  IFS='-' read -a latest_date_arr <<< "$latest_commit_date"
  latest_year=${latest_date_arr[0]}
  #echo $latest_year
  latest_month=${latest_date_arr[1]}
  mod_latest_month=${latest_month#0} # strip leading 0
  #echo $mod_latest_month
  latest_day=${latest_date_arr[2]}
  #echo $latest_day
  # echo "******************************"
  alu=`git log --pretty=format:%H | tail -1`
  first_commit_date=`git log -1 --date=short --pretty=format:%cd $alu`
  # echo "First commit date:"
  # echo $first_commit_date
  IFS='-' read -a first_date_arr <<< "$first_commit_date"
  first_year=${first_date_arr[0]}
  #echo $first_year
  first_month=${first_date_arr[1]}
  mod_first_month=${first_month#0} # strip leading 0
  #echo $mod_first_month
  first_day=${first_date_arr[2]}
  #echo $first_day
  # echo "******************************"
  diff_year=$(( latest_year - first_year ))
  diff_year_months=$(( diff_year*12 ))
  #echo "Diff year in months: $diff_year_months"
  diff_month=$(( mod_latest_month - mod_first_month ))
  #echo "Diff  months: $diff_month"
  if [ $diff_month -gt 0 ]
  then
    total_month_diff=$(( diff_year_months + diff_month ))
  else
    if [ $diff_month -eq 0 ]
    then
        # echo "Number is Zero!"
        total_month_diff=$(( diff_year_months + diff_month ))
    else
        # echo "Number is Negative!!"
        mod_diff_month=$(( 12 + $diff_month ))
        total_month_diff=$(( diff_year_months + mod_diff_month ))
    fi
  fi
  #echo "total diff in month: $total_month_diff"
  total_commit_count=`git rev-list --count master`
  # echo "Total commit count: $total_commit_count"
  echo "$repo_name,$first_commit_date,$latest_commit_date,$total_commit_count"
  # echo "========================================================="
  ## get out of the repo name
  cd ..
  # echo "----------------------------------------------------------------------------"
done < "$1"
