from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib3

chromeOptions = webdriver.ChromeOptions()

# Path for where you want to download the files
prefs = {"download.default_directory" : "  "}
chromeOptions.add_experimental_option("prefs",prefs)

#Path for your chrome driver
pchromdriver = '/usr/lib/chromium-browser/chromedriver'
browser = webdriver.Chrome(executable_path = pchromdriver, chrome_options=chromeOptions)

url = 'https://dsc.orbund.com/einstein-freshair/student_frameset.jsp'
browser.get(url)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

user = ' ' #username goes here
pw = ' ' #password goes here 

username.send_keys(user)
password.send_keys(pw)

select = Select(browser.find_element_by_name('role'))

# Enter 1 for student, 3 for instructor, 4 for admin or 6 for staff
select.select_by_value(' ')
browser.find_element_by_id("loginBtn").click()

fileid = 150950 #Enter initial file id
while(fileid < 150990): #Enter your ending file id
	url = 'https://dsc.orbund.com/einstein-freshair/getfile.jsp?fileid='
	final_url = ''.join([url, str(fileid)])
	browser.get(final_url)
	fileid += 1

browser.close()