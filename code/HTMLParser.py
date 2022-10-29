from operator import contains
from bs4 import BeautifulSoup

# general test file header
header = "documents/"
mail_identifier = "mailto:"

# files we'll be using for testing
test_pages = tuple(["naturalscipage.html", "cockrellpage.html", "anthropologypage.html"])
page_names = tuple(["Natural_Sci_Emails", "Cockrell_Engineering_Emails", "Anthropology_Emails"])

# headers for file creation
DIRECTORY_HEADER = "email_files/"
FILE_TYPE = ".txt"


# TODO
# listing which school/college each set of emails is from
# get the web scraper to work
# figure out the upload process (get all the emails onto a document or spreadsheet)

# loop through list of pages
for page_index in range(len(test_pages)):
    # convert page into beautifulSoup object
    with open("documents/" + test_pages[page_index], encoding="utf-8") as myPage:
        soup = BeautifulSoup(myPage, features="html.parser")

    all_link_tags = soup.findAll('a') # get all link tags
    STORAGE_FILE = DIRECTORY_HEADER + page_names[page_index] + FILE_TYPE

    # create a new email file
    try:
        with open(STORAGE_FILE, 'x') as email_file:
            for tag in all_link_tags:
                # loop through all 'a' tags, check if it has an email attribute'
                #Cockrell & Natural Science method
                attributeList = tag.get_attribute_list('href')

                # does this element contain an href attribute?
                if (attributeList[0] is None):
                    continue
                else:
                    ref_string = attributeList[0]

                    # do any hrefs in this element contain mail links?
                    if len(ref_string) > 6 and ref_string[0:6] == "mailto":
                        an_email = ref_string[7:len(ref_string)]
                        email_file.write(an_email + "\n")
    except: 
        # if the file already exists, simply skip it
        print("Skipped creation of file: " + STORAGE_FILE)
        continue
        
            


            



 
