# Scratch Scraper

**This repository hosts all the code that was used for the bachelor's thesis [*Scraping Scratch: A Dataset of Comments and their Sentiment (2020)*](https://github.com/dyonende/Scratch-scraper/blob/master/Thesis%20Final%20Version.pdf) by Dyon van der Ende and supervised by Fenia Aivaloglou.**

The goal of this research was to create a dataset that contains Scratch comments labelled with sentiment.
The data can be found here: 
- [sqlite3 database](https://drive.google.com/file/d/1roo16yDH7hUGmrYMKqIGWWTjmM1QL069/view?usp=sharing)
- [csv](https://drive.google.com/drive/folders/1Qo1KzRfSiEqD-69peGp601XMQ59YtF9o?usp=sharing)

## tools
All tools are written in Python.
Here only a brief overview of the tools is given. For a more complete description please read the Methods section in the thesis.
Also a complete description of the data can be found there.

### [projectscraper.py](https://github.com/dyonende/Scratch-scraper/blob/master/projectscraper.py)
This program takes a list of project ids of Scratch projects and downloads the available meta-data of the project in JSON format. This is then parsed and written to stdout in csv-format.

### [commentscraper.py](https://github.com/dyonende/Scratch-scraper/blob/master/commentscraper.py)
This program takes a file with on each line "\[username\] \[projectID\] \[comments\]" as input and will then download and parse the comments and meta-data of the comments and print this to stdout. 
The comments is used to skip projects that have no comments, but if the number of comments is not available, just put any number greater than 0 in order to still process the project.

### [replyscraper.py](https://github.com/dyonende/Scratch-scraper/blob/master/replyscraper.py)
This program works almost the same as the comment scraper, but downloads and parses the replies to a comment. 
Therefore, instead of heaving a number of comments as input, it takes a file with on each line "\[username\] \[projectID\] \[commentID\]"), where commentID is the comment that the replies should be downloaded of.

### [langanote.py](https://github.com/dyonende/Scratch-scraper/blob/master/langanote.py)
This program has as input a csv file containing the output of commentscraper.py or replyscraper.py. It analyses every comment with pycld2 and adds the language of the comment in a new column, also in csv format to stdout.

---

*Disclaimer: the tools are not tested to work under different circumstances other than the exact described way in the thesis. It is possible that it requires adjustment to work properly for you!*

 
