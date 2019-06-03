#rm -r */     ---> removes all the folders from the directory containing all the profile.html pages
from bs4 import BeautifulSoup
import os
import re
from details import company_details, company_name
import math
import csv


EMAIL_REGEX = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?" 
#r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
linkedin_profile_data = []
linkedin_company_data = []
global company_score_dict
company_score_dict = {}
global company_elo_score_dict
company_elo_score_dict = {}

def get_profiles(directory="./profiles"):
	profiles = os.listdir(directory)
	return profiles

def filter_companies(list1):
	exclusion_list = set(['Üniversitesi','university','institute','school','University','Institute','School','Education','education','Engineering','engineering'])
	exclusion_list = [i.lower() for i in exclusion_list]
	filtered=[]
	for i in list1:
		if not any(map(lambda x:x in i.lower(), exclusion_list)):
			filtered.append(i)
	filtered = filtered[::-1]#reverse left->right ----->increasing reputation
	return filtered

def naive_company_score(companies):
	global company_score_dict
	for pos,company in enumerate(companies):
		if company not in company_score_dict:
			company_score_dict[company] = pos + 1
		else:
			company_score_dict[company] += pos + 1

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def elo_score(rating1, rating2, p1=1, k=32):
	p1_wins = 1/(1 + math.pow(10,(rating2-rating1)/400))
	p2_wins = 1/(1 + math.pow(10,(rating1-rating2)/400))
	if p1 == 1:#if player 1 wins
		new_rating1 = rating1 + k*(1 - p1_wins)
		new_rating2 = rating2 + k*(0 - p2_wins)
	else:
		new_rating1 = rating1 + k*(0 - p1_wins)
		new_rating2 = rating2 + k*(1 - p2_wins)

	return new_rating1, new_rating2

def initialize_elo_scores(companies):
	global company_elo_score_dict
	for pos,company in enumerate(companies):
		if company not in company_elo_score_dict:
			company_elo_score_dict[company] = 1000
		else:
			continue

def get_company_elo_ratings(company_list):
	companies = filter_companies(company_list)#doing this 2 times straightens it up
	unique_companies = f7(companies)
	initialize_elo_scores(unique_companies)
	x = zip(unique_companies, unique_companies[1:])
	for i,j in x:
		company_elo_score_dict[i], company_elo_score_dict[j] = elo_score(company_elo_score_dict[i],company_elo_score_dict[j])


def scrape_company_scores():
	for profile in profiles[:]:
		soup = BeautifulSoup(open("./profiles/"+profile, encoding='utf-8'), 'html.parser')
		list1 = company_name(soup)
		companies_only = filter_companies(list1)#left<right
		naive_company_score(companies_only)
		get_company_elo_ratings(companies_only)
	#create file
	myfile = open('company_scores.csv', 'w', encoding = 'utf-8')
	wr = csv.writer(myfile)
	wr.writerow(['Company Name','Naive Score','ELO score'])
	for company in company_score_dict.keys():
		x = company_score_dict[company]
		y = company_elo_score_dict[company]
		#print(company,str(x),str(y))
		wr.writerow([company,x,y])
	myfile.close()


# mast=sorted( ((v,k) for k,v in company_elo_score_dict.items()), reverse=True)
# for i,k in mast[:10]:
# 	print(i,k)

profiles = get_profiles()
# def get_details(profiles):
# 	#name #current_status #email #companies #companies with description
def scrape_info(profiles):
	for profile in profiles[:]:
		try:
			print(profile)
			soup = BeautifulSoup(open("./profiles/"+profile, encoding='utf-8'), 'html.parser')
			name = soup.title.string.replace("(1) ","").replace(" | LinkedIn","")
			current_status = soup.find_all('h2',{'class':["pv-top-card-section__headline", 'mt1 inline-block t-18 t-black t-normal']}, limit=1)[0].next.strip()
			email = re.search(EMAIL_REGEX, soup.text)# re.findall(EMAIL_REGEX,soup.text) --> to find all emails in a page
			if not email:
				email = ''
			else:
				email = email.group(0)
			#get companies and exclude universities
			list1 = company_name(soup)#[soup.find_all('span', class_="pv-entity__secondary-title")[i].next.strip() for i in range(len(soup.find_all('span', class_="pv-entity__secondary-title")))]
			companies = filter_companies(list1)
			companies = companies[::-1]#straighten up
			companies = " | ".join(companies)
			#get_company_elo_ratings(companies)
			details = company_details(soup)
			linkedin_profile_data.append([name, current_status, companies, details, email])
		
		except:
			print("PROBLEM FOUND IN "+ profile)
			#os.remove("./profiles/"+profile)
	return linkedin_profile_data

linkedin_profile_data = scrape_info(profiles)


#print(company_elo_score_dict)

def create_csv(list1):
	with open('Linkedin_data.csv', 'w', encoding = 'utf-8') as myfile:
		wr = csv.writer(myfile)
		wr.writerow(['Name', 'Current Status', 'Company Arsenal', 'Internship/Job Details', 'Email'])
		for i in list1:
			wr.writerow(i)

create_csv(linkedin_profile_data)


def create_html():
	html_str = """
	<html>
	<body>
	<table border=1>
	<tr><th>Name</th><th>Current Status</th><th>Companies</th><th>Details</th><th>Email</th></tr>
	"""
	with open("filename.html","w") as Html_file:
		Html_file.write(html_str)
		for i in linkedin_profile_data:
			Html_file.write("<tr>")
			Html_file.write("<td>"+ i[0] + '</td>')
			Html_file.write("<td>"+ i[1] + '</td>')
			Html_file.write("<td>"+ i[2] + '</td>')
			Html_file.write("<td>"+ i[3] + '</td>')
			Html_file.write("<td>"+ i[4] + '</td>')
			Html_file.write("</tr>")
		Html_file.write("</table></body></html>")

	



#