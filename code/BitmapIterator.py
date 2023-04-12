

class BitmapIterator:
    index = 0
    shift = 0
    bitmap = None
    mapping = None
    length = None
    onZero = None

    def __init__(self, bitmap, mapping, length, matchOnZero = True):
        if mapping is None:
            raise Exception("the mapping cannot be None")

        self.bitmap = int(bitmap)
        self.mapping = mapping
        self.length = int(length)
        self.onZero = bool(matchOnZero)

    @staticmethod
    def reverse_bitmap(bmap, len):
        rev = '{:04b}'.format(bmap, width=len)
        print(str(bmap))
        print(rev)
        return int(rev[::-1], 2)

    def forward(self):
        if self.shift >= self.length :
            raise Exception("Index out of bounds error")

        self.shift = self.shift + 1
        bit = (self.bitmap << self.shift) & 0b1

        if bit != self.onZero:
            self.index = self.index + 1
            return self.mapping[self.index]

    def refresh(self):
        self.index = 0
        self.shift = 0

    def flip_match_bit(self):
        self.onZero = not self.onZero

