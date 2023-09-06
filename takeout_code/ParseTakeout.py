import csv
from mailbox import mbox as mb
import mimetypes

# from StringTools import extractNameAndEmail
from NETStringTools import extractUsingReplyTo
from NETStringTools import ListToString

EMAIL_OUTPUT_PATH = 'takeout_files/net_member_emails.csv'
EMAIL_INPUT_PATH = 'takeout_files/NEW_MEMBER.mbox'
CONTENT_LOCATOR = 'This is a multi-part message in MIME format.'
COLUMNS = ['EMAIL', 'FIRSTNAME', 'LASTNAME', 'SMS', 'GENDER']

netbox = mb(EMAIL_INPUT_PATH, factory=None, create=False)
# print(mimetypes.guess_type("EMAIL_INPUT_PATH"))

with open(EMAIL_OUTPUT_PATH, 'w') as csvfile:
    # writing to csv file
    fwriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    fwriter.writerow(COLUMNS)

    SUBSCRIBER_INFO = ["", "", "", "", 0]
    for iterations, message in enumerate(netbox):
        mfrom = message.as_string()
        credentials = extractUsingReplyTo(mfrom)   

        if credentials is None:
            print("Couldn't find 'Name:' in message")
            print(mfrom)
            break

        num_credentials = len(credentials)
        SUBSCRIBER_INFO[0] = ''.join(credentials[len(credentials) - 1]) # EMAIL EXTRACTION
        SUBSCRIBER_INFO[1] = ''.join(credentials[0]) # FIRST NAME EXTRACTION
        if num_credentials > 2: SUBSCRIBER_INFO[2] = ListToString(credentials, 1) # LAST NAME EXTRACTION
        fwriter.writerow(SUBSCRIBER_INFO)



