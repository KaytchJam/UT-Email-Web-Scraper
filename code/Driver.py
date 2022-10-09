from selenium.webdriver.edge.service import Service
from selenium import webdriver

service = Service(executable_path="C:\Users\kaytc\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# navigating to web page (opening it)
# driver.get("https://liberalarts.utexas.edu/academics/departments.html")
# driver.back() to go back a page