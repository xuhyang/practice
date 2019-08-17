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

    def sort(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1, [0 for _ in range(len(nums))])

    def mergeSort(self, nums, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        self.merge(nums, start, mid, end, temp)

    def merge(self, nums, start, mid, end, temp):
        left, right, index = start, mid, start

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left <= mid:
            nums[index] = nums[left]
            left += 1
            index += 1

        while right <= end:
            nums[index] = nums[right]
            right += 1
            index += 1

        for i in range(start, end):
            nums[i] = temp[i]


    def sort2(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, start, end):
        if start >= end:
            return

        pivot = nums[(start + end) // 2]
        left, right = start, end

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
