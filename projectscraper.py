# @author: Dyon van der Ende
#input file: file with projectID on each line
#output: csv format with header to stdout

import requests
import json
import sys
import pathlib

if len(sys.argv) < 2:
    print("please use \"python3 projectscraper.py [ProjectIDs]\" to download projects")
    sys.exit
elif len(sys.argv) == 2:
    print("author_id; author_username; project_id; title; comments_allowed; date_created; date_modified; date_shared; visible; views; loves; favorites; comments; remixes")
    with open(sys.argv[1]) as file:
        for line in file:
            projectID = line.rstrip('\n')
            try:
                url = "https://api.scratch.mit.edu/projects/"+projectID
                r = requests.get(url, allow_redirects=True)
                file = r.content
                line = json.loads(file)
                try:
                    id = line['id']
                    title = line['title']
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
