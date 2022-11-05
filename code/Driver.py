import email
from logging import NullHandler
from sre_parse import WHITESPACE
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from operator import contains
from bs4 import BeautifulSoup

from HTMLParser import Email_Parser
from HTMLParser import Liberal_Arts_Parser

DRIVER_PATH = r"C:\Users\kaytc\edgedriver_win64\msedgedriver.exe"
service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Edge(service=service)

# Next Page Parser
# Liberal Arts Parser
# Sub Page Parser

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
    # driver.implicitly_wait(5)
    # driver.get("https://liberalarts.utexas.edu/academics/departments.html")
    # department_list = driver.find_element(By.CLASS_NAME, "offices-list")
    # dpt_links = Liberal_Arts_Parser.get_department_links(driver.page_source)

    # for dpt in dpt_links:
    #     print(dpt)
    #     header = "https://liberalarts.utexas.edu"
    #     driver.get(header + dpt)
    #     get_nav = driver.find_element(By.ID, "main-nav")
    #     nav_items = get_nav.find_elements(By.TAG_NAME, "a")
    #     delay = 4

    #     print("waiting for faculty element")
    #     try:
    #         # this is filler to get the page to load
    #         filler_element = WebDriverWait(driver, delay).until(EC.text_to_be_present_in_element((By.TAG_NAME, "a"), " Faculty & Research " ))
    #     except TimeoutException:
    #         print("Took too long")

    #     faculty = Liberal_Arts_Parser.get_faculty_link(driver.page_source)
    #     if faculty is None: continue
    #     driver.get(header + faculty)
    #     delay = 9 # seconds

    #      # print("waiting")
    #     try:
    #         filler_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "fac-info")))
    #     except TimeoutException:
    #         print("Took too long")
        
    #     html = driver.find_element(By.TAG_NAME, "html")
    #     outer_html = html.get_attribute("outerHTML")
    #     s = BeautifulSoup(outer_html, features='html.parser')
    #     print("writing to file")
    #     all_tags = BeautifulSoup(outer_html, features='html.parser').findAll('a')

    #     # print("EMAIL SET: ")
    #     try:
    #         with open("email_files" + dpt + ".txt", 'x') as email_file:
    #             EP = Email_Parser("mailto", email_file)
    #             EP.email_stream(EP.write_to_file, all_tags)
    #     except FileExistsError:
    #         continue

    next_page_directories = tuple(["https://cns.utexas.edu/directory/items/1-directory", "https://pharmacy.utexas.edu/directory",
                                    "https://lbj.utexas.edu/faculty-lbj-school-public-affairs", "https://socialwork.utexas.edu/directory/", 
                                    "https://dellmed.utexas.edu/directory?page=1"])
    directory_names = tuple(["naturalscience", "pharmacy", "lbjpublic", "stevehickssocial", "dellmedical"])
    DELLMED_NEXT_CONSTANT = "javascript:void(0)"

    counter = -1
    for directory in next_page_directories:
        counter = counter + 1
        driver.get(directory)
        print(directory_names[counter])
        current_link = directory

        try:
            with open("email_files/" + directory_names[counter] + ".txt", 'x') as email_file:
                EP = Email_Parser("mailto", email_file)
                while current_link is not None:
                    driver.get(current_link)

                    all_tags = BeautifulSoup(driver.page_source, features="html.parser").findAll('a')
                    write_made = EP.email_stream(EP.write_to_file, all_tags)

                    # were any files written ?
                    if write_made == False:
                        print("no writes made, try other method")
                        break # temporary solution is to break till i actually work on it 

                    next_link = EP.get_next(driver.page_source)
                    if next_link is not None:
                        if next_link == DELLMED_NEXT_CONSTANT:
                            print(page_number)
                            page_number = int(current_link[len(current_link)-1:len(current_link)]) + 1
                            next_link = current_link[0:len(current_link)-1] + str(page_number)
                        # General case
                        else: next_link = directory + EP.remove_until_character(next_link, '?')
                    current_link = next_link
        except FileExistsError:
            print("File " + directory_names[counter] + " already exists.")
            continue

except NotImplementedError:
    print("Problem?")
    driver.quit()
    counter = 1


driver.quit()

