import time;
from selenium import webdriver;

#time refresh
Timer = 3 #(3seconds)

#youtube link
link = 'https://www.youtube.com/watch?v=oOaP0hBbRJk&feature=youtu.be'

#number
views = 30

driver.get(link)

for i in range(views):
	time.sleep(Timer)
	driver refresh()
