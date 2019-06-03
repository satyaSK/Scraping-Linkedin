import re
from bs4 import BeautifulSoup
import os
import sys

# lines=[]

# print(lines[:10])

def get_profiles(directory="./profiles"):
	profiles = os.listdir(directory)
	return profiles

def get_profiles_from_profiles(profile_page):
	links=[]
	soup = BeautifulSoup(open("./profiles/"+profile_page, encoding='utf-8'), 'html.parser')
	try:
		for a in soup.find_all('a',{'class':["pv-browsemap-section__member ember-view"]}, href=True):
			links.append(a['href'])
	except:
		print("CAN'T FETCH LINKS FROM "+profile_page)
	
	return links

def get_links_of_links():
	links_of_links = []
	profiles = get_profiles()
	for i in profiles:
		links_of_links.extend(get_profiles_from_profiles(i))

	links_of_links = list(set(links_of_links))#remove duplicates

	with open("links_of_links.txt",'w') as text_file:
		for i in links_of_links:
			text_file.write(i+"\n")

	return links_of_links, len(links_of_links)


##### To get connection links from the downloaded profiles(2nd degree connections) #####

# a,b = get_links_of_links()
# print(b)



# linkedin_profiles = get_linkedin_profiles(lines)
# print(linkedin_profiles[:15])


# links= get_profiles_from_profiles('profile0.html')
# print(links)