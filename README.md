# UT-Email-Web-Scraper
### What is this for?

#### Web Scrapper for consolidating a bunch of emails from various UT Austin departments. The emails are being collected using the Beautiful Soup and Selenium Python libraries. 

### Todo List: 

-[ ] Implementing the Selenium Edge Driver 
-[ ] Extracting emails from all the pages (where it can be done without selenium)
-[ ] Adding all the emails to the drive
-[ ] Figuring out how to automate the email sending process (?)

#### Faculty pages that need to be handled with Selenium

1. College of Education
2. Mccombs School of Business 
3. College of Pharamacy
4. Dell Medical School
5. LBJ School of Public Affairs
6. Moody College of Communication https://moody.utexas.edu/faculty
7. School of Architecture https://soa.utexas.edu/about/faculty
8. School of Information https://www.ischool.utexas.edu/people/ischool-faculty-staff-students

#### Faculty pages that don't need Selenium

1. Cockrell School of Engineering
2. College of Fine Arts
3. College of Natural Sciences
4. Jackson School of Geosciences
5. Graduate School Staff
6. School of Law
7. School of Nursing
8. Steve Hicks School of Social Work

#### Special Cases

- The College of Liberal Arts

The college of liberal arts encapsulates multiple departments (school of anthropology, history, linguistics, etc.). Each indiviudal department can be 
parsed without using Selenium, however, accessing each faculty page in a timely manner would best be done using Selenium.



