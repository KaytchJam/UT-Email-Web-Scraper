import email
from operator import contains
from bs4 import BeautifulSoup

header = "documents/"
test_pages = tuple(["samplesite.html", "cockrellpage.html", "anthrpologypage.html"])

#with open("documents/cockrellpage.html", encoding='UTF-8') as myFile:
 #   soup = BeautifulSoup(myFile, features="html.parser",)

# Printing Tag fields
# tag = soup.h
# print(tag)
# print(type(tag))
# print(tag.name)

# loop through list of pages
for page_index in range(len(test_pages)):
    # convert page into beautifulSoup object
    with open("documents/" + test_pages[page_index], encoding="utf-8") as myPage:
        soup = BeautifulSoup(myPage, features="html.parser")

    all_a = soup.findAll('a')
    counter = 1
    email_list = list()

    for tag in all_a:
        # loop through all 'a' tags, check if it has an email attribute'
        #Cockrell & Natural Science method
        attributeList = tag.get_attribute_list('href')
        print(attributeList)

        if "email" in tag.get_attribute_list('class'):
            #print(str(counter) + ".")
            #email_string = tag.string
            #email_list.append(email_string)
            #print("Email: " + email_string + "\n")
            counter += 1
 
