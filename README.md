# Scraping Linkedin 
The problem is that, when students(like myself) are in search of internships, they want to get get answers to the following questions: 
* What does a list of really good(possibly relatively less known) companies look like?
* Can I get a list of really good companies I have never heard of?
* What do interns at these companies work on? What is their responsibility?
* Where are top university students interning at? What are the kind of opportunities they are exposed to?
* How can I get a rough idea about the quantitative measure of the goodness of all these companies? (This repo rates the companies using ELO score and a Naive score)
* What are the previous companies of students who have interned at top companies?

Finding answers to these questions is possible, but very time consuming. In no time, students find themselves stuck in the monotonous task of querying through Linkedin profiles and trying to assimmilate huge chunks of information. 
This code repository is a bunch of scripts. Its a fast and dirty way which would allow students to scrape Linkedin for educational purposes. It would allow students to look at potential internship/job opportunities and responsibilities
at a variety of different companies more easily. It makes the internship/job hunting experience a little less cumbersome. **It allows students to optimally target the best companies according to what they want to actually do, without having 
to send out 100-200 applications to random companies just to gain some work ex.**

## Dependencies
* beautifulsoup4
* pyautogui


Use the ```pip install <package>``` command to install the dependencies.

## Pipeline
```
1fetch_public_links to google custom search -> 2download_profiles to download Linkedin profiles -> 3linkedin_parser to scrape data for educational purposes -> a CSV containing internship/job data will be created in your current directory -> 4linkedin_extras(optional) to extract links of links
```

# Steps to Excecute

## Step 1
Create a directory, name it ```scraping```. This will be your working directory at all times. Within this directory create a directory named `profiles`. Make sure that you have setup your google custom search engine and the [generate your API key](https://developers.google.com/custom-search/v1/overview) and [Google search engine ID](https://cse.google.com/cse/all). NOTE: Toggle the ```Search the entire web``` to ```ON```

## Step 2
Create 2 ```.txt``` files. One will hold a list of top domain-specific colleges(For example:Stanford, UCB, CMU etc), and the other would hold a list of well-known companies in your field. Give these files a name. For now, let's call them ```companies.txt``` and ```colleges.txt```. Make sure that the every company name is on a new line in the text file. Same for colleges.

## Step 3
Open cmd in current directory and type:
```
python 1fetch_public_links.py companies colleges
```
This will create 2 files in your current directory. 
```
query_list.txt --> contains all the query result links from the Google custom search.
linkedin_list.txt --> contains only Linkedin profile links.
```

## Step 4
Now type in cmd:
```
python 2download_profiles.py 
```
Note that you might need to make small tweaks in this file. You should change all time related parameters such as ```time.sleep()``` and ```pyautogui.PAUSE``` to suite your download speed. You can run the above command after you have made these changes. Wait and watch. Profiles will open and source code will be downloaded. You will have all the profiles downloaded to your profiles directory. Keep only the profile HTML pages in the profiles directory.

## Step 5
Now type:
```
python 3linkedin_parser.py companies colleges
```
This will create a CSV file of all the scraped data in an easily readable format. To get an idea of the quantitative measure of the goodness of each company, you can also run the ```company_scores()``` function to get a CSV containing a naive score and an [ELO score](https://en.wikipedia.org/wiki/Elo_rating_system) of all the companies. You can sort the CSV file according to either of the scores to get an idea of how good the companies are. These scores are based on the assumption that the latest work experience is better than the work experience before it.

## Step 6
You can play around with the code to get the most out of it. I have included functions which scrape all the available data for student use. 
