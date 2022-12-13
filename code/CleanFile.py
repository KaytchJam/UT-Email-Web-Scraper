
file1 = 'mccombsbusiness_foo.txt'
file2 = 'mccombsbusiness.txt'

prefix = "email_files/"
with open(prefix + file1, 'r') as source:

    counter = 1
    # copy over all odd numbered files
    with open(prefix + file2, 'x') as dest:
        for line in source:
            if counter == 2:
                counter = counter >> 1
                continue
            dest.write(line)
            counter = counter << 1
