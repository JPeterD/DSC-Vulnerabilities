from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib3

#Path to your chromedriver
pchromdriver = '/usr/lib/chromium-browser/chromedriver'
browser = webdriver.Chrome(executable_path = pchromdriver)

url = 'https://dsc.orbund.com/einstein-freshair/student_frameset.jsp'
browser.get(url)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

user = ' ' # your username goes here
pw = ' ' # your password goes here 

username.send_keys(user)
password.send_keys(pw)


select = Select(browser.find_element_by_name('role'))

#1 for student, 3 for instructor, 4 for admin, 6 for staff

select.select_by_value(' ')
browser.find_element_by_id("loginBtn").click()

#Crates text file studentnames.txt to store userid(for pictures) and Full Name
file = open("studentnames", "w")

#Starting Student ID to store
studentid = 15400

while(studentid < 15405): #Enter the ending student ID
  url = 'https://dsc.orbund.com/einstein-freshair/print_progressreport.jsp?studentid='
  trailing = '&semesterid=59&classid=12500&subjectid=11125&sortOrder=0&sortingColumn=testDate'

  final_url = ''.join([url, str(studentid), trailing])
  browser.get(final_url)
  try:
    student = browser.find_element_by_xpath("//html/body/table[1]/tbody/tr[3]/td[2]")
  except:
    print("This user does not exist")
    studentid +=1
  else:
    student = student.text
    file.write("\n" + student + "    " + str(studentid))
    studentid += 1

file.close()
browser.close()