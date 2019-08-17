class array:
    def findMedianSortedArrays(self, a, b):
        n = len(a) + len(b)

        if n % 2 == 1:
            return self.findKth(a, 0, b, 0, n // 2 + 1) # find kth not index k
        return (self.findKth(a, 0, b, 0, n // 2) + self.findKth(a, 0, b, 0, n // 2 + 1)) / 2

    def findKth(self, a, aIndex, b, bIndex, kth):
        if aIndex == len(a):
            return b[bIndex + kth - 1]
        if bIndex == len(b):
            return a[aIndex + kth - 1]
        if kth == 1:
            return min(a[aIndex], b[bIndex])
                        #kth to index
        halfKthOfA = a[aIndex + kth // 2 - 1] if aIndex + kth // 2 - 1 < len(a) else sys.maxsize
        halfKthOfB = b[bIndex + kth // 2 - 1] if bIndex + kth // 2 - 1 < len(b) else sys.maxsize

        if halfKthOfA < halfKthOfB:                              #kth could be odd 5 - 2 =3
            return self.findKth(a, aIndex + kth // 2, b, bIndex, kth - kth // 2)
        return self.findKth(a, aIndex, b, bIndex + kth // 2, kth - kth // 2 )

    
