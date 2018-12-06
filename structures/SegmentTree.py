# pylint: disable=invalid-name

""" Implementation of a segment tree. """

class SegmentTree():
    def __update(self, old, upd):
        return old + upd

    def __query(self, left, right):
        return min(left, right)

    def __init__(self, size, update = None, query = None):
        self.__update = update or self.__update
        self.__query = query or self.__query
        self.size = size
        self.seg = [0] * (2 * size)

    def update(self, p, upd):
        """ Update position p with value upd. """
        p += self.size
        self.seg[p] = self.__update(self.seg[p], upd)
        while p != 1:
            self.seg[p >> 1] = self.__query(self.seg[p], self.seg[p ^ 1])
            p >>= 1

    def query(self, l, r):
        """ Get query result in range [l, r]. """
        l, r = l + self.size, r + self.size
        result = self.seg[l]
        while l < r:
            if l & 1:
                result = self.__query(result, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                result = self.__query(result, self.seg[r])
            l, r = l >> 1, r >> 1
        return result
