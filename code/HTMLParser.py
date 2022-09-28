from bs4 import BeautifulSoup

with open("documents/samplesite.html") as myFile:
    soup = BeautifulSoup(myFile, features="html.parser")

# Printing Tag fields
# tag = soup.h
# print(tag)
# print(type(tag))
# print(tag.name)

all_a = soup.findAll('a')
print(all_a)

counter = 1
for tag in all_a:
    print(str(counter) + ".")
    print("tag name " + tag.name)
    print("tag: ", end="")
    print(tag)
    print("tag attributes: ", end="")
    print(tag.attrs)
    print("tag contents: ", end="")
    print(tag.contents)
    print("tag children: ", end="")
    print(tag.children)
    print("tag descendants: ", end="")
    print(tag.descendants)
    print("tag string: ", end="")
    print(tag.string)
    counter += 1
