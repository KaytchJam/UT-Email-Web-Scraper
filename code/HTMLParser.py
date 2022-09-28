import email
from operator import contains
from bs4 import BeautifulSoup

with open("documents/cockrellpage.html", encoding='UTF-8') as myFile:
    soup = BeautifulSoup(myFile, features="html.parser",)

# Printing Tag fields
# tag = soup.h
# print(tag)
# print(type(tag))
# print(tag.name)

all_a = soup.findAll('a')
#print(all_a)

counter = 1

email_list = list()

for tag in all_a:
    # loop through all 'a' tags, check if it has an email attribute
    if "email" in tag.get_attribute_list('class'):
        print(str(counter) + ".")
        email_string = tag.string
        email_list.append(email_string)
        print("Email: " + email_string + "\n")
        counter += 1

