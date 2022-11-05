# UT-Email-Web-Scraper
### What is this for?

#### Web Scraper for consolidating a bunch of emails from various UT Austin departments. The emails are being collected using the Beautiful Soup and Selenium Python libraries. 

![Give me your emails](https://github.com/KaytchJam/UT-Email-Web-Scraper/blob/main/documents/give_me_your_email_expanded.png?raw=true)

### Todo List: 

- [x] Implementing the Selenium Edge Driver 
- [x] Extracting emails from all the pages (where it can be done without selenium)
- [ ] Figure out In-N-Out Selenium navigation method
- [x] Extracting emails from most of the Liberal Arts Directories
- [ ] Adding all the emails to the drive
- [ ] Figuring out how to automate the email sending process (?)

### Checklist:
- [x] Cockrell School of Engineering
- [x] Jackson School of Geoscience
- [x] College of Fine Arts
- [x] Texas School of Law
- [x] School of Nursing
- [x] Steve Hicks School of Social Work
- [x] College of Natural Sciences
- [ ] School of Architecture
- [ ] School of Information
- [ ] College of Pharamacy
- [ ] Mccombs School of Business
- [x] Dell Medical School
- [ ] LBJ School of Public Affairs
- [ ] Moody College of Communication

### Liberal Arts Checklist:
- [x] African Studies
- [x] Air & Air Space Force Science
- [x] American Studies
- [x] Anthropology
- [x] Asian Studies
- [x] Classics
- [x] Economics
- [x] English
- [x] French and Italian
- [ ] Geography & Environment
- [x] Germanic Studies
- [x] Government
- [x] History
- [x] Linguistics
- [x] Mexican American and Latina/o Studies
- [x] Middle Eastern Studies
- [ ] Military Science
- [x] Naval Science
- [ ] Philosophy
- [x] Pyschology
- [ ] Religious Studies
- [x] Rhetoric and Writing
- [x] Slavic & Eurasian Studies
- [x] Sociology
- [x] Spanish & Portugeuse

#### Faculty pages that need to be handled with Selenium

1. College of Education
2. Mccombs School of Business 
3. College of Pharamacy
4. Dell Medical School
5. LBJ School of Public Affairs
6. Moody College of Communication https://moody.utexas.edu/faculty
7. School of Architecture https://soa.utexas.edu/about/faculty
8. School of Information https://www.ischool.utexas.edu/people/ischool-faculty-staff-students

#### Faculty pages that don't need Selenium (Maybe just a way to go the next page)

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



