#use: python3 readcsv.py [allProjects.csv] [lim]
#input file: csv file 
#output: projectID
import csv
import sys

with open(sys.argv[1]) as csv_file:
    lim = -1
    counter = 0
    if len(sys.argv) is 3:
        lim = int(sys.argv[2])
        
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[1])
        counter = counter + 1
        if lim > 0 and counter > lim:
            sys.exit()