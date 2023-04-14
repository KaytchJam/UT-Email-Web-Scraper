import pandas as pd
from BitmapIterator import BitmapIterator
import PConstants

# newFrame = pd.DataFrame({0:[1, 2, 3],1:[4, 5, 6],2:[7,8,9]})
# print(newFrame)

src_dir = "email_files/"

filler = pd.DataFrame({'Department':[], 'Liberal_Arts':[], 'Inverse':[]})
r_map = BitmapIterator.reverse_bitmap(PConstants.GROUP_BITMAP, PConstants.LENGTH)
zeroIt = BitmapIterator(r_map, PConstants.LENGTH, PConstants.ZERO_MAPPINGS)
oneIt = BitmapIterator(r_map, PConstants.LENGTH, PConstants.ONE_MAPPINGS, False)

index = 0
COMBINED_SUM = len(PConstants.ZERO_MAPPINGS) + len(PConstants.ONE_MAPPINGS)
while not zeroIt.at_end or not oneIt.at_end():
    zeroVal = ['-', None]
    oneVal = ['-', None]

    if not zeroIt.at_end(): zeroVal = zeroIt.forward_pair()
    if not oneIt.at_end(): oneVal = oneIt.forward_pair()

    if (not zeroVal[0]) or oneVal[0]:
        if not zeroVal[0]: filler.loc[index, :] = [zeroVal[1], False, COMBINED_SUM - index - 1]
        else: filler.loc[index, :] = [oneVal[1], True, COMBINED_SUM - index - 1]
        index = index + 1

print(filler)

print(filler.groupby('Department.').all())

libs = filler.loc[(filler.loc[:,'Liberal Arts.'] == True)]
print(libs)