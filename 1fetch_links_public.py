from googleapiclient.discovery import build
import sys
import re
from bs4 import BeautifulSoup
import os

my_api_key = #######
my_cse_id = ######

companies_txt_file_path = sys.argv[1]
colleges_txt_file_path = sys.argv[2]
output_filename = 'query_links.txt'

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	return res['items']

def getLists(companies_txt_file_path, colleges_txt_file_path):
	with open(companies_txt_file_path + '.txt','r') as file1:
		companies = file1.read().split('\n')

	with open(colleges_txt_file_path + '.txt','r') as file2:
		colleges = file2.read().split('\n')

	return companies, colleges


def getLinks(companies_list, colleges_list, output_filename):
	#companies_list = ['Kelley','CMU','UWash','Eller','Texas AMU']
	#colleges_list = ['MS in information systems','MIS','business analyst', 'technology analyst', 'data analyst', 'analytics consultant', 'technology consultant', 'data science']
	queries=[]

	for i in companies_list:
		for j in colleges_list:
			q = i +" "+ j +" "+'intern linkedin'
			results = google_search(q, my_api_key, my_cse_id, num=10)
			queries.append(results)
	
	with open(output_filename, 'w') as textfile:
		for query in queries:
			for result in query:
				textfile.write(result['link']+"\n")

def get_linkedin_profiles(lines):
	p = re.compile("(.*)linkedin.com/in/(.*)")
	linkedin_profiles = []
	for i in lines:
		if p.match(i):
			linkedin_profiles.append(i)

	return linkedin_profiles

def filterLinks():
	with open( output_filename ,'r') as text_file:
		lines = text_file.read().split('\n')

	linkedin_profiles = get_linkedin_profiles(lines)

	with open('linkedin_links.txt','w') as txt:
		for link in linkedin_profiles:
			txt.write(link+"\n")


a,b = getLists(companies_txt_file_path, colleges_txt_file_path)
getLinks(a,b, output_filename)
filterLinks()

	
