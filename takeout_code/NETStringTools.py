
def string_stream(string, start, end, f):
    while start < end:
        f(string[start])
        start += 1
    
# Extraction function -> uses Name: and Email: to find names and emails
def extractNameAndEmail(mbox_string):
    if not isinstance(mbox_string, str) or mbox_string == None:
        raise TypeError("mbox_string must be a string")
    
    # CONSTANTS
    NAME = "Name:"
    EMAIL = "Email:"
    STR_END = len(mbox_string)
    TARGETS = [NAME, EMAIL]
    SEARCH = True
    
    # POINTERS (INDICES)
    stream_ptr = mbox_string.find(NAME)
    initial = stream_ptr
    string_ptr = 0
    tgt_index = 0
    data_index = 0

    if (initial == -1): return None
    data = [] # where our names will be stored

    while (stream_ptr < STR_END and tgt_index < 2):

        cur_char = mbox_string[stream_ptr] # current index in string
        offset = stream_ptr - initial
        print(f"{offset} : {cur_char}")

        if offset > 100: return []
       
        if SEARCH:  # looking for the next "Name:" or "Email:"
            if cur_char == TARGETS[tgt_index][string_ptr]:
                string_ptr += 1
            else: string_ptr = 0

            if string_ptr == len(TARGETS[tgt_index]):
                SEARCH = False
                string_ptr = 0
                stream_ptr += 1
                data.append([])

        else: # we are in the middle of a name or email (SEARCH == FALSE)
            if cur_char == '\n': 
                SEARCH = True
                data_index += 1
                tgt_index += 1
            else:
                if cur_char == ' ':
                    data_index += 1
                    stream_ptr += 1
                    data.append([])
                    continue
                data[data_index].append(cur_char)

        stream_ptr += 1

    return data

# Revised extraction function -> uses Reply-To: instead of Name: and Email:
def extractUsingReplyTo(mbox_string):
    if not isinstance(mbox_string, str) or mbox_string == None:
        raise TypeError("mbox_string must be a string")
    
    # CONSTANTS
    REPLY_TO = "Reply-To: "
    STR_END = len(mbox_string)
    EMAIL_INDICATOR = "<>"
    IGNORE = ["\"", "\\"]

    # POINTERS (INDICES)
    stream_ptr = mbox_string.find(REPLY_TO)
    indicator_ptr = 0
    data_index = 0

    if stream_ptr == -1: return None
    stream_ptr += len(REPLY_TO)

    data = [[]]
    while stream_ptr < STR_END and indicator_ptr < len(EMAIL_INDICATOR):
        cur_char = mbox_string[stream_ptr]
        if cur_char == EMAIL_INDICATOR[indicator_ptr]:
            indicator_ptr += 1
        else:
            if cur_char == ' ':
                data_index += 1
                data.append([])
            elif cur_char not in IGNORE:
                data[data_index].append(cur_char)
        stream_ptr += 1

    return data

# Converts a list of strings into a single string
def ListToString(li, start_index = 0):
    if not isinstance(li, list):
        raise TypeError("li must be a list")
    
    LENGTH = len(li) - 1
    ptr = start_index
    s = ''
    while ptr < LENGTH:
        if ptr < LENGTH - 1:
            li[ptr].append(' ')
        s += ''.join(li[ptr])
        ptr += 1
    return s


            



