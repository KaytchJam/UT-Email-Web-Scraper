import email
from operator import contains
from bs4 import BeautifulSoup

header = "documents/"
test_pages = tuple(["samplesite.html", "cockrellpage.html", "anthropologypage.html"])

# Printing Tag fields
# tag = soup.h
# print(tag)
# print(type(tag))
# print(tag.name)

counter = 1
# loop through list of pages
for page_index in range(len(test_pages)):
    # convert page into beautifulSoup object
    with open("documents/" + test_pages[page_index], encoding="utf-8") as myPage:
        soup = BeautifulSoup(myPage, features="html.parser")

    all_a = soup.findAll('a')
    email_list = list()

    for tag in all_a:
        # loop through all 'a' tags, check if it has an email attribute'
        #Cockrell & Natural Science method
        attributeList = tag.get_attribute_list('href')

        if len(attributeList) < 1:
            continue
        else:
            ref_string = attributeList[0]
            if ref_string[0:6] == "mailto":
                print(str(counter) + ".")
                print(ref_string)
                counter += 1


            



 
