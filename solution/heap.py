class heap:

    def heapify(self, nums):
        for i in range((len(nums) - 1) // 2, -1 , -1):
            self.siftDown(nums, i)

    def siftDown(self, nums, i):
        while i < len(nums):
            son = i * 2 + 1
            if i * 2 + 2 < len(nums) and nums[i * 2 + 2] < nums[son]:
                son = i * 2 + 2
            if nums[son] >= nums[i]:
                break

            nums[son], nums[i] = nums[i], nums[son]
            i = son




