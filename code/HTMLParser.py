from bs4 import BeautifulSoup
from sqlalchemy import null;

with open("documents/samplesite.html") as myFile:
    soup = BeautifulSoup(myFile, features="html.parser")

tag = soup.h
print(tag)
print(type(tag))