from bs4 import BeautifulSoup

def company_details(profile_page_soup):
	profile_details = ['']
	#print(len(profile_page_soup.find_all('div', class_="pv-entity__position-group-pager pv-profile-section__list-item ember-view")))
	for i in profile_page_soup.find_all('div', class_="pv-entity__position-group-pager pv-profile-section__list-item ember-view"):
		try:
			company = i.find('span', class_="pv-entity__secondary-title").get_text(" ",strip=True)
		except:
			if i.find('div', class_="pv-entity__company-summary-info"):
				company = i.find('div', class_="pv-entity__company-summary-info")#.get_text(" ",strip=True)
				company = company.find('span', class_="").get_text(" ",strip=True)
			else:
				company = ""
		#print(company)
		if i.find('h3', class_="t-16 t-black t-bold"):#.get_text(" ",strip=True)
			position = i.find('h3', class_="t-16 t-black t-bold").get_text(" ",strip=True)
		else:
			position = ''
		#print(position)

		if i.find('p', class_="pv-entity__description"):
			description = i.find_all('div', class_="pv-entity__extra-details ember-view")#.get_text(" ",strip=True).replace(" ... See more",'')#find('p', class_="pv-entity__description")
			description = [j.get_text(" ",strip=True).replace(" ... See more",'') for j in description]
			description = " ".join(description)
		else:
			description = ''

		full_text = company + " ==> " + position + " ==> " + str(description)
		#print(full_text+"\n\n")
		profile_details.append(full_text)
	return "\n\n* ".join(profile_details)


def company_name(soup):
	all_companies = []
	#print(len(soup.find_all('div', class_="pv-entity__position-group-pager pv-profile-section__list-item ember-view")))
	for i in soup.find_all('div', class_="pv-entity__position-group-pager pv-profile-section__list-item ember-view"):
		try:
			company = i.find('span', class_="pv-entity__secondary-title").get_text(" ",strip=True)
		except:
			if i.find('div', class_="pv-entity__company-summary-info"):
				company = i.find('div', class_="pv-entity__company-summary-info")#.get_text(" ",strip=True)
				company = company.find('span', class_="").get_text(" ",strip=True)
			else:
				company = ""
		all_companies.append(company)
	return all_companies



# soup = BeautifulSoup(open("./profiles/Julia Gong _ LinkedIn.html", encoding='utf-8'), 'html.parser')

# x = company_name(soup)
# print(x)