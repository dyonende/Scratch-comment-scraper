#input file: csv file 
#output: projectID
import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    skipfirstline = True
    for row in csv_reader:
        if skipfirstline is True: 
            skipfirstline = False
        else:
            print(row[1], row[2], row[12])