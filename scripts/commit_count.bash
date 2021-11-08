#!/bin/bash
cat repo_path.txt | while read line 
do
   # do something with $line here
    cd $line; echo $line >> commit_count.txt; git rev-list --all --count >> commit_count.txt; cd 
done
