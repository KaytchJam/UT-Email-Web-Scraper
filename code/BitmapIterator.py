

class BitmapIterator:
    index = -1
    shift = 0
    bitmap = None
    mapping = None
    length = None
    onZero = None

    def __init__(self, bitmap, length, mapping, matchOnZero = True):
        if mapping is None:
            raise Exception("the mapping cannot be None")

        self.bitmap = int(bitmap)
        self.mapping = mapping
        self.length = int(length)
        self.onZero = bool(matchOnZero)

    @staticmethod
    def reverse_bitmap(bmap, len):
        rev = '{:04b}'.format(bmap, width=len)
        rev = int(rev[::-1], 2)
        return rev

    def forward_pair(self):
        if self.at_end():
            raise Exception("Out of bounds error")

        self.shift = self.shift + 1

        bit = (self.bitmap >> self.shift) & 0x1
        if bit != self.onZero:
            self.index = self.index + 1
            return (bit, self.mapping[self.index])
        return (bit, None)

    def forward(self):
        return self.forward_pair()[1]
    
    def current_bit(self):
        if self.at_bitmap_end():
            raise Exception("Out of bitmap error")
        return (self.bitmap << self.shift) & 0b1

    def refresh(self):
        self.index = 0
        self.shift = 0

    def flip_match_bit(self):
        self.onZero = not self.onZero
    
    def at_bitmap_end(self):
        return self.shift >= self.length
    
    def at_mapping_end(self):
        return self.index >= (len(self.mapping) - 1)

    def at_end(self):
        return self.at_mapping_end() or self.at_bitmap_end()
