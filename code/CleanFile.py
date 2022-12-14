import os 
from queue import PriorityQueue
from HTMLParser import Email_Parser

# file1 = 'mccombsbusiness_foo.txt'
# file2 = 'mccombsbusiness.txt'
# pfix = "email_files/"

class FileWrapper():
    file = None
    fileName = ""

    def __init__(self, file):
        self.file = file
        self.fileName = str(file.name)
    
    def __lt__(self, other):
        return self.fileName < other.fileName

    def __gt__(self, other):
        return self.fileName > other.fileName

    def __eq__(self, other):
        return self.fileName == other.fileName
    
    def __str__(self) -> str:
        return self.fileName
    
    def getFilename(self):
        return self.fileName
    
    def getFile(self):
        return self.file


def write_to_another(f1, f2, prefix = "email_files/", skipEveryOther = False):
    with open(prefix + f1, 'r') as source:

        counter = 0
        if skipEveryOther: counter = 1
        # copy over all odd numbered files
        with open(prefix + f2, 'x') as dest:
            for line in source:
                if counter == 2:
                    counter = counter >> 1
                    continue
                dest.write(line)
                counter = counter << 1

# write_to_another(file1, file2, pfix, True)

# Returns a read-only list of files from a given path
def get_directory_files(path):
    if os.path.isdir(path) is False: return None # base case
    directory_filenames = os.listdir(path)

    read_only_files = list()
    for filename in directory_filenames:
        read_only_files.append(open( path + "/" + filename, 'r'))
    return read_only_files

# Merge all text files content into a singular "semi" sorted text file
def merge_and_sort_txtfiles(file_list, arr):
    canWrite = True
    q = PriorityQueue()
    formerFile = None

    while canWrite:
        if q.empty() == False:
            formerLine = formerFile.getFile().readline()
            if formerLine != "":
                q.put((formerLine, formerFile))
        else:
            for file in file_list:
                line = file.readline()
                if line != "":
                    q.put((line, FileWrapper(file)))
                    canWrite = True
        
        if q.empty() == False:
            filePair = q.get()
            arr.append(filePair[0])
            formerFile = filePair[1]
        else: canWrite = False

# Coalesce all the written files into a single sorted text file
# Important thing to note, the original text files themselves are not sorted, and so I opted for this method to get a "somewhat" sorted list
# and then a full sort of the entire list afterwards
LOCAL_PATH = "email_files"
FILES_TO_READ = get_directory_files(LOCAL_PATH)
with open("email_files/all_emails.txt", 'x') as dest:
    myList = list()
    merge_and_sort_txtfiles(FILES_TO_READ, myList) # somewhat sorts the list
    myList.sort(key=str.lower) # fully sorts the list
    myMap = {}
    for line in myList:
        if myMap.get(line) is None:
            myMap[line] = 1
            dest.write(line)

