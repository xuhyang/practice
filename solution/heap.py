class Heap:

    def heapify(self, nums):
        # (len(nums) - 1) // 2 or len(nums) // 2 or len(nums) // 2 - 1 all okay
        for i in range(len(nums) // 2, -1, -1):
            self.siftDown(nums, i)

    def siftDown(self, nums, i):
        #check if left child will be out of index, not i < len(nums)
        while i * 2 + 1 < len(nums):
            son = i * 2 + 1
            if son + 1 < len(nums) and nums[son + 1] < nums[son]:
                son += 1
            if nums[i] <= nums[son]:
                break

            nums[i], nums[son] = nums[son], nums[i]
            i = son
