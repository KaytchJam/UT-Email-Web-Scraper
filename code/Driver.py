from selenium.webdriver.edge.service import Service
from selenium import webdriver
from operator import contains
from bs4 import BeautifulSoup

DRIVER_PATH = "C:\Users\kaytc\edgedriver_win64\msedgedriver.exe"
service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Edge(service=service)

# navigating to web page (opening it)
# driver.get("https://liberalarts.utexas.edu/academics/departments.html")
# s = beautifulSoup(driver.page_source, 'html.parser')
# driver.back() to go back a page

# navigate the liberal arts departments page:
    # get the <div class=offices-list> element
        # get all the <div class="offices-item"> tags
            # go to the <h3> <a href="/aads"></a></h3>
            # add the link to the end of the current url
            # get all emails 
            # go back and repeat with next office-item tag

driver.get("https://liberalarts.utexas.edu/academics/departments.html")
s = BeautifulSoup(driver.page_source, 'html.parser')

