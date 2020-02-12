#!/bin/sh
mkdir output
echo readcsv
python3 readcsv.py allProjects.csv 10 > ./output/projectIDs.txt
echo projectscraper
python3 projectscraper.py ./output/projectIDs.txt > ./output/project_info.csv 
echo readcsv2
python3 readcsv2.py ./output/project_info.csv > ./output/projects.txt
echo commentscraper
python3 commentscraper.py ./output/projects.txt > ./output/comments.csv
echo done
