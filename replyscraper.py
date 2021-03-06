# @author: Dyon van der Ende
# use: python3 replyscraper.py [commentlist]
# to print all comments from the projects.
#input file: on each line [project_author_username] [project_id] [comment_id]
#output: csv file of comments with header 


import requests
import json
import sys
import pathlib
import html
from decimal import Decimal


#no input file
if len(sys.argv) != 2:
    print("input error")
    sys.exit()
    
#print header
print("project_id;project_author;comment_author_id;comment_author_username;comment_id;comment_parent;commentee_id;comment_date_created;comment_date_modified;visible;comment_content")

linecount = 0
length = len(list(open(sys.argv[1])))
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
        oscounter = 0   #offset counter
        offset = str(oscounter)
        counter = 1
        stepsize = 40
        end = False
        
        line = line.split(' ')
        try:
            user = line[0]
            project = line[1]
            comment = line[2].strip()
        except KeyboardInterrupt:
                sys.exit()
        except:
            print("input line format error", file=sys.stderr)
            
        while end is False:
            try:
                url = "https://api.scratch.mit.edu/users/"+user+"/projects/"+project+"/comments/"+comment+"/replies?offset="+offset+"&limit="+str(stepsize)
                r = requests.get(url, allow_redirects=True)
                if str(r.content).find("[]") >= 0:
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
                                    
                                    sep=';'
                                )
                    except KeyboardInterrupt:
                        sys.exit()
                    except:
                        end = True;
                    oscounter+=stepsize
                    offset = str(oscounter)
                counter+=1
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("failure", user, project, file=sys.stderr)
print("done!           ", file=sys.stderr)
