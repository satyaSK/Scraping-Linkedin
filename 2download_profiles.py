#rm -r */     ---> removes all the folders from the directory containing all the profile.html pages
import webbrowser
import pyautogui
import time
import re
import sys

scan_file = ''
if len(sys.argv) > 1:
    scan_file = sys.argv[1]
else:
    scan_file = 'linkedin_links.txt'

lines=[]

with open(scan_file,'r') as text_file:
	lines = text_file.read().split('\n')
# url = "https://www.linkedin.com/in/willhang/"
# webbrowser.open(url)
# time.sleep(5)
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True
# hrefs = get_linkedin_profiles(lines)
def get_profiles(directory="./profiles"):
	profiles = os.listdir(directory)
	return profiles

def scrape_html(hrefs,n=5):
	c = 1425
	for link in hrefs[:n]:
		try:
			url = link
			webbrowser.open(url)
			time.sleep(4)
			pyautogui.keyDown('ctrl')
			pyautogui.press('s')
			pyautogui.keyUp('ctrl')
			name ='profile'+str(c)
			pyautogui.typewrite(name, 0.01)
			pyautogui.press('enter')
			time.sleep(9)
			pyautogui.keyDown('ctrl')
			pyautogui.press('w')
			pyautogui.keyUp('ctrl')
			print("Done profile "+str(c))
			c+=1
		except:
			print("MISSED "+str(c))
			continue


scrape_html(lines)
print("{0} Linkedin Profiles Downloaded".format(len(lines)))

# pyautogui.keyDown('ctrl')
# pyautogui.press('s')
# pyautogui.keyUp('ctrl')
# pyautogui.typewrite('profile2', 0.1)
# pyautogui.press('enter')
# time.sleep(10)
# pyautogui.keyDown('ctrl')
# pyautogui.press('w')
# pyautogui.keyUp('ctrl')




# print("#####")