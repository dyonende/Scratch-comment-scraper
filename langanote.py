# @author:  Dyon van der Ende
# input:    csv file from commentscraper.py or replyscraper.py
# output:   input;language;reliable
from __future__ import print_function
import csv
import sys
import pycld2 as cld2
import nltk
import re
import traceback
from decimal import Decimal
from nltk.corpus import words

#test if nltk words is downloaded otherwise download
try:
	"test" in words.words()
except:
	nltk.download('words')


#print csv header
print("project_id;project_author;comment_author_id;comment_author_username;comment_id;comment_parent;commentee_id;comment_date_created;comment_date_modified;visible;comment_content;language;reliable")


linecount = 0
length = len(list(open(sys.argv[1])))
with open(sys.argv[1]) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	skipfirstline = True    #set to false if csv has no header
	for row in csv_reader:
        #show progress
		dots = ""
		for dot in range(0, linecount%4):
			dots = dots + "."
		for dot in range (linecount%4, 4):
			dots = dots + " "
		print(" "+str(round(Decimal(100*linecount/length),2))+"%"+dots , end='\r', file=sys.stderr)
		linecount = linecount+1
        
        #skip header line
		if skipfirstline is True: 
			skipfirstline = False
		else:
			try:
				isReliable, textBytesFound, details = cld2.detect(row[10])  #language detection with cld2
				lang = details[0][1]
                #workaround for short sentences (less than 4 words)
                #if all (max.) 3 words are in the nltk words list, then consider the text as english
				if len(row[10].split())<4 and details[0][1]=='un':
					for word in row[10].split():
						if ("".join(e for e in word if e.isalpha())).lower() in words.words():
							lang = 'en'
							isReliable = True
						else:
							lang = details[0][1]
							isReliable = False
							break
						
				content = "\""+row[10]+"\""
					
				print(
						row[0],
						row[1],
						row[2],
						row[3],
						row[4],
						row[5],
						row[6],
						row[7],
						row[8],
						row[9],
						content,
						lang,
						isReliable,

						sep=';' #csv delimiter
				)

			except KeyboardInterrupt:
				sys.exit()
			except Exception:
				traceback.print_exc()
				print("failure: ", row, file=sys.stderr)
print("done", file=sys.stderr)
