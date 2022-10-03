import email
from operator import contains
from bs4 import BeautifulSoup

# general test file header
header = "documents/"
mail_identifier = "mailto:"
# files we'll be using for testing
test_pages = tuple(["samplesite.html", "cockrellpage.html", "anthropologypage.html"])

# TODO
# listing which school/college each set of emails is from
# get the web scraper to work
# figure out the upload process (get all the emails onto a document or spreadsheet)

counter = 1
# loop through list of pages
for page_index in range(len(test_pages)):
    # convert page into beautifulSoup object
    with open("documents/" + test_pages[page_index], encoding="utf-8") as myPage:
        soup = BeautifulSoup(myPage, features="html.parser")

    all_a = soup.findAll('a') # get all link tags
    email_list = list()

    for tag in all_a:
        # loop through all 'a' tags, check if it has an email attribute'
        #Cockrell & Natural Science method
        attributeList = tag.get_attribute_list('href')

        if len(attributeList) < 1:
            continue #skip
        else:
            ref_string = attributeList[0]
            if len(ref_string) > 6 and ref_string[0:6] == "mailto":
                email = ref_string[8:len(ref_string)]
                print(str(counter) + "." + email)
                email_list.append(email)
                counter += 1


            



 
