from io import TextIOWrapper
from operator import contains
from bs4 import BeautifulSoup
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Email_Parser:
    DIRECTORY_HEADER = "email_files"
    MAIL_IDENTIFIER = "mailto"
    DEST_FILE = None

    # constructor 
    def __init__(self, MAIL_STRING_IDENTIFIER = "mailto", DESTINATION_FILE = None):
        self.MAIL_IDENTIFIER = MAIL_STRING_IDENTIFIER
        self.set_destination_file(DESTINATION_FILE)
    
    # change the specified destination file
    def set_destination_file(self, DESTINATION_FILE = None):
        if isinstance(DESTINATION_FILE, TextIOWrapper) == False:
            print("DESTINATION_FILE IS NOT A PROPER FILE and will be set to NONE")
            self.DEST_FILE = None
        else:
            self.DEST_FILE = DESTINATION_FILE

    # write to the file that you set
    def write_to_file(self, some_string):
        if self.DEST_FILE is None:
            print("Could not write to file, as destination file is None. Please set destination file.")

        self.DEST_FILE.write(some_string + "\n")
    
    # removes any leading whitespace in a given string
    def clean_up_leading_whitespace(some_string = "   test"):
        if some_string is None:
            return None
        
        WHITESPACE = " "
        while some_string[0] == WHITESPACE:
            some_string = some_string[1:len(some_string)]
        return some_string
    
    # from a given list of Beautiful Soup tags, return a stream of strings of emails contained in the tags and perform "operation" on them
    def email_stream(self, operation = write_to_file, tag_list = None):
        if tag_list is None:
            print("tag list is None")
            return 
        
        for tag in tag_list:
            attr_list = tag.get_attribute_list("href")
            if attr_list[0] is None:
                continue
            else:
                current_href_string = attr_list[0]
                if len(current_href_string) > 6 and current_href_string[0:6] == "mailto":
                    email_string = current_href_string[7:len(current_href_string)]
                    # print(email_string)
                    operation(email_string)

# helps parse the stuff on the liberal arts page
class Liberal_Arts_Parser:

    # return a list of links to each department page
    def get_department_links(page_HTML):

        soup = BeautifulSoup(page_HTML, features="html.parser")
        o_list = soup.findAll('section', class_="offices-list") # the offices list element
        o_list = o_list[0].findAll('div', class_="offices-item") # list of office items

        department_links = list()
        for o_item in o_list:
            item_link = o_item.a
            department_links.append(item_link['href'])
        return department_links

    # return the link that takes us to the faculty page for a given department
    def get_faculty_link(page_HTML):
        print("here")
        soup = BeautifulSoup(page_HTML, features="html.parser")
        nav_list = soup.findAll('nav', class_="subnav")
        print(nav_list)
        nav_list = nav_list[0].findAll('a')
        print(nav_list)
        print("nav loop")
        for nav_link in nav_list:
            print(nav_link['href'])
            if "faculty" in nav_link['href']:
                return nav_link['href']
        
        return None


    def _failed_preconditions(driver, d_list_or_link):
        if d_list_or_link is None:
            print("department list/link is none")
            return True
        elif driver is None:
            print("driver is none")
            return True
        return False

    # navigate to a liberal art department's faculty page from a given department link
    def get_to_faculty_page_outerHTML(self, driver, department_link):
        if self._failed_preconditions(driver, department_link):
            return None

        driver.get(department_link.get_property('href'))
        get_nav = driver.find_element(By.ID, "main-nav")
        nav_items = get_nav.find_elements(By.TAG_NAME, "a")
        faculty_nav_item = nav_items[1]
        driver.get(faculty_nav_item.get_property("href"))
        delay = 5 #seconds 
        try:
            filler_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "fac-info")))
        except TimeoutException:
            print("Took too long")

        html = driver.find_element(By.TAG_NAME, "html")
        return html.get_attribute("outerHTML")

        
            


        
            


            



 
