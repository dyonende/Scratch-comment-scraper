# @author: Dyon van der Ende
# use:  python3 commentscraper.py [projectlist]
#       to print all comments from the projects.
#       input file: on each line "[username] [projectID] [comments]"
#       if comments=0 the line will be skipped. If the amount of comments
#       is unknown, put any value greater than 0 and the line will not be skipped
#output: csv file of comments with header 


import requests
import json
import sys
import pathlib
import html
from decimal import Decimal


#no input file provided
if len(sys.argv) != 2:
    print("input error")
    sys.exit()
    

#print the csv header
print("project_id;project_author;comment_author_id;comment_author_username;comment_id;comment_parent;commentee_id;comment_date_created;comment_date_modified;visible;comment_content")

linecount = 0   #current line
length = len(list(open(sys.argv[1])))    #total number of lines
with open(sys.argv[1]) as file:    
    for line in file:
        #show progress
        dots = ""
        for dot in range(0, linecount%4):
            dots = dots + "."
        for dot in range (linecount%4, 4):
            dots = dots + " "
        print(" "+str(round(Decimal(100*linecount/length),2))+"%"+dots , end='\r', file=sys.stderr)
        linecount = linecount+1
        
        
        user = ""
        project = ""
        oscounter = 0   #offset
        offset = str(oscounter)
        counter = 1
        stepsize = 40   #40 is maximum
        end = False
        comments = 0
        
        line = line.split(' ')
        try:
            user = line[0]
            project = line[1]
            comments = int(line[2])
        except KeyboardInterrupt:
                sys.exit()
        except:
            print("input line format error: [username] [projectID] [comments]", file=sys.stderr)
            
        if comments > 0:    #skip projects without comments
            while end is False:
                try:
                    url = "https://api.scratch.mit.edu/users/"+user+"/projects/"+project+"/comments?offset="+offset+"&limit="+str(stepsize)
                    r = requests.get(url, allow_redirects=True)
                    if str(r.content).find("[]") >= 0: #empty JSON file means no (more) comments
                        end = True
                    else:
                        file = r.content
                        data = json.loads(file)
                        try:
                            for line in data:
                                id = line['id']
                                parent_id = line['parent_id']
                                commentee_id = line['commentee_id']
                                content = " ".join(line['content'].split())
                                content = "\"" + content + "\""
                                date_created = line['datetime_created']
                                date_modified = line['datetime_modified']
                                visibility = line['visibility']
                                author_id = line['author']['id']
                                author_username = "\"" + line['author']['username'] + "\""
                                print(  project,
                                        user,
                                        author_id,
                                        author_username,
                                        id,
                                        parent_id,
                                        commentee_id,
                                        date_created,
                                        date_modified,
                                        visibility,
                                        content,
                                        
                                        sep=';' #csv delimter
                                    )
                        except KeyboardInterrupt:
                            sys.exit()
                        except:
                            print("parse error: ", line, file=sys.stderr)
                            end = True;
                        oscounter+=stepsize
                        offset = str(oscounter)
                    counter+=1
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    print("failure", user, project, file=sys.stderr)
print("done", file=sys.stderr)           
