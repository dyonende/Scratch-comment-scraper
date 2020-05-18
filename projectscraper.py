# @author: Dyon van der Ende
# input: file with projectID on separate line
# output: csv format with header to stdout

import requests
import json
import sys
import pathlib
from decimal import Decimal

if len(sys.argv) < 2:
    print("please use \"python3 projectscraper.py [ProjectIDs]\" to download projects")
    sys.exit
elif len(sys.argv) == 2:

    print("author_id;author_username;project_id;title;comments_allowed;date_created;date_modified;date_shared;visible;views;loves;favorites;comments;remixes")
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
            
            projectID = line.rstrip('\n')
            try:
                url = "https://api.scratch.mit.edu/projects/"+projectID
                r = requests.get(url, allow_redirects=True)
                file = r.content
                line = json.loads(file)
                try:
                    id = line['id']
                    title = "\"" + line['title'] + "\""
                    visibility = line['visibility']
                    comments_allowed = line['comments_allowed']

                    date_created = line['history']['created']
                    date_modified = line['history']['modified']
                    date_shared = line['history']['shared']

                    author_id = line['author']['id']
                    author_username = "\"" + line['author']['username'] + "\""

                    views = line['stats']['views']
                    loves = line['stats']['loves']
                    favorites = line['stats']['favorites']
                    comments = line['stats']['comments']
                    remixes = line['stats']['remixes']
                    if comments_allowed == True:
                        print(  
                                author_id,
                                author_username,
                                id,
                                title,
                                comments_allowed,
                                date_created,
                                date_modified,
                                date_shared,
                                visibility, 
                                views,
                                loves,
                                favorites,
                                comments,
                                remixes,

                                sep=';'
                            )
                except:
                    print("invalid file: ", filename, file=sys.stderr)
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("failure", projectID, file=sys.stderr)
elif len(sys.argv) == 3:
    print("author_id;author_username;project_id;title;comments_allowed;date_created;date_modified;date_shared;visible;views;loves;favorites;comments;remixes")
    max_projects = int(sys.argv[2]) #maximum number of projects to download
    count = 0
    linecount = 0
    length = max_projects
    with open(sys.argv[1]) as file:
        for line in file:
            dots = ""
            for dot in range(0, linecount%4):
                dots = dots + "."
            for dot in range (linecount%4, 4):
                dots = dots + " "
            print(" "+str(round(Decimal(100*linecount/length),2))+"%"+dots , end='\r', file=sys.stderr)
            linecount = linecount+1
            if count == max_projects:
                sys.exit()
            projectID = line.rstrip('\n')
            try:
                url = "https://api.scratch.mit.edu/projects/"+projectID
                r = requests.get(url, allow_redirects=True)
                file = r.content
                line = json.loads(file)
                try:
                    id = line['id']
                    title = "\"" + line['title'] + "\""
                    visibility = line['visibility']
                    comments_allowed = line['comments_allowed']

                    date_created = line['history']['created']
                    date_modified = line['history']['modified']
                    date_shared = line['history']['shared']

                    author_id = line['author']['id']
                    author_username = "\"" + line['author']['username'] + "\""

                    views = line['stats']['views']
                    loves = line['stats']['loves']
                    favorites = line['stats']['favorites']
                    comments = line['stats']['comments']
                    remixes = line['stats']['remixes']
                    if comments_allowed == True:
                        print(  
                                author_id,
                                author_username,
                                id,
                                title,
                                comments_allowed,
                                date_created,
                                date_modified,
                                date_shared,
                                visibility, 
                                views,
                                loves,
                                favorites,
                                comments,
                                remixes,

                                sep=';'
                            )
                    count = count + 1
                except:
                    print("invalid file: ", filename, file=sys.stderr)
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("failure", projectID, file=sys.stderr)
print("done", file=sys.stderr)
