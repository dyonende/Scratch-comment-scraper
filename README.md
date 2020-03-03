automate.sh will execute the following commands:

$ python3 readcsv.py allProjects.csv [lim] > ./output/projectIDs.txt

$ python3 projectscraper.py ./output/projectIDs.txt > ./output/project_info.csv 

$ python3 readcsv2.py ./output/project_info.csv > ./output/projects.txt

$ python3 commentscraper.py ./output/projects.txt > ./output/comments.csv

the file projectIDs.txt contains only a list of project id's extracted from the allProjects.csv dataset.

project_info.csv contains all information of a project extracted from the json file downloaded from the scratch website. 
This step is necessary to obtain the usernames, which is required in the next step to download comments.

projects.txt contains a list of projects with the usernames attached.

comments.csv has formatted the json file that was downloaded from the scratch website into a csv file with all information about the comments. 
This is the file that will be used to further analyse the comments.

All files will be stored in ./output/ 

The [lim] parameter (currently set to 10 in automate.sh) allows to set a maximum to the number of projects downloaded.
