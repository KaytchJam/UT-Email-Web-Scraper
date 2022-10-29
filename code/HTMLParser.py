from operator import contains
from bs4 import BeautifulSoup

# general test file header
header = "documents/"
MAIL_IDENTIFIER = "mailto:"

# files we'll be using for testing
SCHOOL_FACULTY_HTML_FILES = tuple(["naturalscipage.html", "cockrellpage.html", "anthropologypage.html", "jacksongeosciencepage.html", "fineartspage.html", "lawschoolpage.html",
                                    "nursingschoolpage.html", "stevehickssocialworkpage.html"])
EMAIL_FILE_NAMES = tuple(["Natural_Sci_Emails", "Cockrell_Engineering_Emails", "Anthropology_Emails", "Jackson_Geoscience_Emails", "Fine_Arts_Emails", "Law_School_Emails"])

# headers for file creation
DIRECTORY_HEADER = "email_files/"
FILE_TYPE = ".txt"


# TODO
# listing which school/college each set of emails is from
# get the web scraper to work
# figure out the upload process (get all the emails onto a document or spreadsheet)

# Selenium Driver is needed for the following faculty pages:
# School of Education
# Mccombs School of Business 
# School of Pharmacy (Austin) https://pharmacy.utexas.edu/people/austin
# Dell Medical School https://intranet.dellmed.utexas.edu/public/committees-and-councils
# LBJ School of Public Affairs https://lbj.utexas.edu/faculty-lbj-school-public-affairs

# ACTUAL HTML PARSING STUFF

# loop through list of pages
for page_index in range(len(SCHOOL_FACULTY_HTML_FILES)):
    # convert page into beautifulSoup object
    with open("documents/" + SCHOOL_FACULTY_HTML_FILES[page_index], encoding="utf-8") as myPage:
        soup = BeautifulSoup(myPage, features="html.parser")

    all_link_tags = soup.findAll('a') # get all link tags
    STORAGE_FILE = DIRECTORY_HEADER + EMAIL_FILE_NAMES[page_index] + FILE_TYPE

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
                    if len(ref_string) > 6 and ref_string[0:6] == MAIL_IDENTIFIER:
                        an_email = ref_string[7:len(ref_string)]
                        email_file.write(an_email + "\n")
    except FileExistsError: 
        # if the file already exists, simply skip it
        print("File already exists: " + STORAGE_FILE)
        continue
        
            


            



 
