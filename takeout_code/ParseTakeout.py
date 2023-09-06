import csv
from mailbox import mbox as mb
import mimetypes

# from StringTools import extractNameAndEmail
from NETStringTools import extractUsingReplyTo
from NETStringTools import ListToString

# CONSTANTS
EMAIL_OUTPUT_PATH = 'takeout_files/net_member_emails.csv'
EMAIL_INPUT_PATH = 'takeout_files/NEW_MEMBER.mbox'
COLUMNS = ['EMAIL', 'FIRSTNAME', 'LASTNAME', 'SMS', 'GENDER'] # CSV FILE COLUMN FORMAT

netbox = mb(EMAIL_INPUT_PATH, factory=None, create=False) # mailbox object

with open(EMAIL_OUTPUT_PATH, 'x') as csvfile:
    # writing to csv file
    fwriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    fwriter.writerow(COLUMNS)

    # Extraction Loop
    Subscriber_Info = ["", "", "", "", 0]
    for iterations, message in enumerate(netbox):
        mfrom = message.as_string()
        credentials = extractUsingReplyTo(mfrom)   

        if credentials is None: # "Error Handling" but not really
            print("Couldn't find 'Reply-To:' in message")
            print(mfrom)
            break
        
        # Row Insertion
        num_credentials = len(credentials)
        Subscriber_Info[0] = ''.join(credentials[len(credentials) - 1]) # EMAIL EXTRACTION
        Subscriber_Info[1] = ''.join(credentials[0]) # FIRST NAME EXTRACTION
        if num_credentials > 2: Subscriber_Info[2] = ListToString(credentials, 1)  # LAST NAME EXTRACTION
        else: Subscriber_Info[2] = ""
        fwriter.writerow(Subscriber_Info)



