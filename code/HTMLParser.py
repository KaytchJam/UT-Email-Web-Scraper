from asyncore import write
from io import TextIOWrapper
from operator import contains
from bs4 import BeautifulSoup
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

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
        write_made = False
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
                    write_made = True
                    operation(email_string)
        return write_made

    # Check if the child element of some tag type of another element in a resultSet (parent_list) has a specified innerText
    def __find_child_with_tag_and_text(self, parent_list = None, tag = None, innerText = None):
        if parent_list is None or tag is None or innerText is None:
            return None

        tag = tag.lower()
        innerText = innerText.lower()

        for parent in parent_list:
            for child_element in parent.findAll(tag):
                if innerText in child_element.getText().lower():
                    return child_element
        return None
    
    def __find_child_with_class_next(self, parent_list = None, tag = None, element_class = None):
        if parent_list is None or tag is None or element_class is None:
            return None

        true_a_list = None
        for parent in parent_list:
            temp_a_list = parent.findAll(tag, class_= element_class)
            if temp_a_list[0] is not None and (true_a_list is None or (len(true_a_list) < len(temp_a_list))):
                true_a_list = temp_a_list
        return true_a_list


        


    # Removes elements from a string from index 0 to the first index of the special character
    def remove_until_character(self, link = None, special_character = "?"):
        if link is None: return None
        while link[0] != special_character:
            link = link[1:len(link)]
        return link

    # Returns the link to the next page in a faculty directory
    def get_next(self, page_HTML):
        soup = BeautifulSoup(page_HTML, features="html.parser")
        regex = re.compile('.*pag.*') # regular expression for elements with "pag" string in class
        div_with_pag = soup.findAll("div", {'class' : regex})
        nav_with_pag = soup.findAll('nav', {'class' : regex})
        
        next_is_class = False
        next_page_a = self.__find_child_with_tag_and_text(div_with_pag, 'a', 'next')
        if next_page_a is None:
            next_page_a = self.__find_child_with_tag_and_text(nav_with_pag, 'a', 'next')
        if next_page_a is None:
            next_page_a = self.__find_child_with_class_next(div_with_pag, 'a', 'next') # exclusive to dell medical page
            next_is_class = next_page_a is None  if False else True


        if next_page_a is not None:
            if next_is_class: return next_page_a # the dell medical case
            ref_list = next_page_a.get_attribute_list("href")
            if ref_list[0] is not None:
                return ref_list[0]
            else: # assume we're on the Steve Hicks site if there's no match
                ref_list = next_page_a.get_attribute_list("data-page")
                return "?_paged=" + ref_list[0]
        return None

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
        soup = BeautifulSoup(page_HTML, features="html.parser")
        nav_list = soup.findAll('nav', class_="subnav")
        nav_list = nav_list[0].findAll('a')

        for nav_link in nav_list:
            print(nav_link['href'])
            if "faculty" in nav_link['href']:
                return nav_link['href']
        
        return None

        
            


        
            


            



 
