from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from operator import contains
from bs4 import BeautifulSoup

DRIVER_PATH = r"C:\Users\kaytc\edgedriver_win64\msedgedriver.exe"
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
try:
    # in the liberal arts general directory
    driver.get("https://liberalarts.utexas.edu/academics/departments.html")
    s = BeautifulSoup(driver.page_source, 'html.parser')
    department_list = driver.find_element(By.CLASS_NAME, "offices-list")
    department_at = department_list.find_element(By.CLASS_NAME, "offices-item")
    department_link = department_at.find_element(By.TAG_NAME, "a")

    # in the AADS department
    driver.get(department_link.get_property('href'))
    print("AT AADS PAGE")
    get_nav = driver.find_element(By.ID, "main-nav")
    nav_items = get_nav.find_elements(By.TAG_NAME, "a")
    faculty = nav_items[1]

    # aads faculty page
    driver.get(faculty.get_property("href"))
    print("AT AADS FACULTY PAGE")
    
    delay = 5 #seconds 
    try:
        filler_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "fac-info")))
    except TimeoutException:
        print("Took too long")

    html = driver.find_element(By.TAG_NAME, "html")
    outer_html = html.get_attribute("outerHTML")
    s = BeautifulSoup(outer_html, features='html.parser')
    all_tags = s.findAll('a')

    print("WE GET DOWN HERE?")
    #print(all_tags)
    for tag in all_tags:
        at_list = tag.get_attribute_list("href")
        if at_list[0] is None:
            continue
        else:
            ref_string = at_list[0]
            if len(ref_string) > 6 and ref_string[0:6] == "mailto":
                print(ref_string[7:len(ref_string)])
            
except:
    driver.quit()
    counter = 1


driver.quit()

