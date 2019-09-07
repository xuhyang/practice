class binarySearch:
#https://www.lintcode.com/problem/last-position-of-target/description?_from=ladder&&fromId=1
#Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#关键字： last position，sorted，array
#思路：因为 暴力解 O(n), sorted，而且array,  所以 binary search
#Time: O(logN), Space O(1)
    def lastPosition(self, nums, target):
        if len(nums) < 1:#always check size
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target: #因为 要求找最后一个target， 所以 找到一个target后继续在右半部分search
                start = mid #因为 当前找到的target可能是最后一个target，所以 将此index保留到下次search
            else:
                end = mid
        #因为 要求找最后一个target，所以 先比较nums[end]再比较nums[start]
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
#https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description?_from=ladder&&fromId=1
#Given a mountain sequence of n integers which, find the mountain top.
#Example 1: #Input: nums = [1, 2, 4, 8, 6, 3] #Output: 8
#关键字：increase firstly and then decrease
#思路：因为 暴力解O(n), 所以binary search. 因为 top定义是 a[top-2]<a[top-1]<a[top]>a[top+1]>a[top+2]，
#所以 当 a[mid]<a[mid+1] top在右边，a[mid]>a[mid-1] top在左边
#因为 increase firstly and then decrease 所以 两个subarray 满足 两个 sorted 条件. OOO即递增，XXX即递减，
#所以 要找 last position of 递增 first position of 递减
#Time: O(logN). SpaceO(n)
    def mountainSequence(self, nums):
        if len(nums) < 1:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < nums[mid + 1]:#如果递增，那么last position of 递增在右边
                start = mid #当前mid可能是最后一位递增 即 top，所以保留到下次search
            else: #如果 递减，那么 first position of 递减 在左边
                end = mid #当前mid可能是第一位递减即 top，所以保留到下次search

        return max(nums[start], nums[end])#缩到两位，比个大小
#https://www.lintcode.com/problem/find-k-closest-elements/description?_from=ladder&&fromId=1
#Given target, a non-negative integer k and an integer array A sorted in ascending order,
#find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target.
#Otherwise, sorted in ascending order by number if the difference is same.
#Example 2: #Input: A = [1, 4, 6, 8], target = 3, k = 3 #Output: [4, 1, 6]
#关键字: sorted, array, non-negative, k closest numbers to target
#思路：因为暴力解 O(n), sorted, array,所以binary search. 因为 k closest， 所以 背向双指针
#Time, O(logN), spaceO(1)
    def kClosestNumbers(self, A, target, k):
        ans = []
        if k == 0:
            return ans

        left, right = 0 , len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2

            if A[mid] < target:
                left = mid
            else:
                right = mid
        #bianry search结束后，target被left和right锁定到最接近的区间
        for _ in range(k):#因为要找k个，所以loop k次，每次移动y一个指针
            #先判断left或right出界，比 判断left和right都没出界 降低了计算量
            if left < 0:
                ans.append(A[right])
                right += 1
            elif right == len(A):
                ans.append(A[left])
                left -= 1
            elif target - A[left] <= A[right] - target:
                ans.append(A[left])
                left -= 1
            else:
                ans.append(A[right])
                right += 1

        return ans
#https://www.lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=1
#Given a big sorted array with non-negative integers sorted by non-decreasing order.
#The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
#Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
#Return -1, if the number doesn't exist in the array.
#Example 1: Input: [1, 3, 6, 9, 21, ...], target = 3 Output: 1
#关键字: sorted, array, can only access the kth number by, Find the first index of a target number
#思路： 因为 sorted，array，find target 所以binary search， 因为array steam 所以倍增
#Time, O(logN), spaceO(1)
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 0
        #因为 array sorted， 所以倍增index， 直到array[index] >= target,
        while reader.get(end) < target:
            end = 2 * end + 1

        while start + 1 < end:
            mid = (start + end) // 2

            if reader.get(mid) < target:
                start = mid
            else: #因为 求first position， 所以 找到target 以后继续向左
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
#https://www.lintcode.com/problem/powx-n/description?_from=ladder&&fromId=1
#also check recursive solution
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        ans, tmp = 1, x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            #x^n = x^(n/2) * x^(n/2)
            tmp *= tmp
            n = n // 2
        return ans
#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).Find the minimum element.
#关键字： sorted, array, rotated.
#思路： 因为 暴力解O(n), sorted array 所以 binary search
#因为 rotated 所以 a[0]<...<a[pivot-2]<a[pivot-1]<a[pivot] > a[pivot+1]<...<a[end-1]<a[end]<a[0]
#因为 binary search 将 arrary 分成两个区间， 所以 pviot 只能在 start-mid区间 或 mid-end区间
#Time: O(logN), Space O(1)
#假设 以start为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[start] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[start] 那么 pivot在 start-end 区间
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        if nums[start] < nums[end]:
            return nums[start]

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= nums[start]:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#假设 以end为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[end] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[end] 那么 pivot在 start-mid 区间, 这个逻辑 也包含了对array没有rotated判断
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#假设 以nums[len(nums)-1]为参照 因为 nums[0]-nums[pivot]满足递增条件OOO nums[pivot]-nums[len(nums)-1] 满足递增条件XXX，所以寻找pivot=寻找first number less than nums[len(nums)-1]
#当 nums[mid]<nums[len(nums)-1], pivot在mid左边， 当 nums[mid]>=nums[len(nums)-1], first number less than nums[len(nums)-1]在mid右边， 所以忽略左边.忽略OOO
     def findMin(self, nums):
        start, end, last = 0, len(nums) - 1
        last = nums[end]

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= last:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#https://www.lintcode.com/problem/fast-power/description?_from=ladder&&fromId=1
#Calculate the a^n % b where a, b and n are all 32bit non-negative integers.
#模运算与基本四则运算有些相似，但是除法例外。其规则如下：
# (a + b) % p = (a % p + b % p) % p （1）
# (a - b) % p = (a % p - b % p + p) % p （2）
# (a * b) % p = (a % p * b % p) % p （3）
# a ^ b % p = ((a % p)^b) % p （4）
    def fastPower(self, a, b, n):
        ans, tmp = 1, a

        while n != 0:
            if n % 2 == 1:
                ans = (ans * tmp) % b
            tmp = (tmp * tmp) % b
            n = n // 2
        return ans % b
#https://www.lintcode.com/problem/find-peak-element/description?_from=ladder&&fromId=1
#There is an integer array which has the following features:
#The numbers in adjacent positions are different. #A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
#We define a position P is a peak if: A[P] > A[P-1] && A[P] > A[P+1]
#Find a peak element in this array. Return the index of the peak.
#关键字：array find a peak element
#思路：因为 暴力解 O(N), 所以 binary search. 因为 已知A[0],A[1]升序 A[n],A[n-1]升序，所以 找mid升序的half
#利用binary search做 排除法
    def findPeak(self, A):
        start, end = 1, len(A) - 2 #or start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid - 1] < A[mid] > A[mid + 1]: #peak found
                return mid
            elif A[mid - 1] > A[mid]: #left has rising order
                end = mid
            else:
                start = mid

        if A[start] > A[end]:
            return start
        return end
#https://www.lintcode.com/problem/first-bad-version/description?_from=ladder&&fromId=1
#The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case,
#so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
#关键字 first，
#思路 因为 暴力解O(N), 所以想到binary search. 因为first 所以 找first position
    def findFirstBadVersion(self, n):
        start, end = 1, n

        while start + 1 < end:
            mid = (start + end) // 2

            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start
        return end
#https://www.lintcode.com/problem/search-in-rotated-sorted-array/description?_from=ladder&&fromId=1
#Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You may assume no duplicate exists in the array.#Example 1:#Input: [4, 5, 1, 2, 3] and target=1, #Output: 2.
#关键字 rotated, sorted array， find target
#思路： 因为 find target in sorted array 所以binary search
    def search(self, A, target):
        if len(A) < 1:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid] < A[end]: #rotation不在mid与end之间
                if A[mid] <= target <= A[end]:#target在升序中，也排除了rotation 那一边
                    start = mid#排除 mid左边
                else:
                    end = mid#target 在rotation那边
            else: # rotation 在mid与end之间
                if A[start] <= target <= A[mid]:#target在升序中，也排除了rotation 那一边
                    end = mid #排除mid右边
                else:
                    start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
