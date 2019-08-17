from collections import deque

class breathFirstSearch:

    def bfs(self, root):
        queue = deque()
        seen = set()

        queue.append(root)
        seen.add(root)

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors():
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)

    def bfsLevel(self, root):
        queue = deque()
        seen = set()

        queue.append(root)
        seen.add(root)

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                for neighbor in node.neighbors():
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)

    def bfsDoubleQueues(self, root):
        queue1, queue2 = deque(), deque()
        seen = set()

        queue1.append(root)
        seen.add(root)
        numLevels = 0
        while queue1:
            size = len(queue1)

            for _ in range(size):
                node = queue1.popleft()
                for neighbor in node.neighbors
                    if neighbor not in seen:
                        queue2.append(neighbor)
                        seen.add(neighbor)

            queue1, queue2 = queue2, queue1
            numLevels += 1

    def bfsDummyNode(self, root):
        queue = deque()
        seen = set()
        numLevels = 0

        queue.append(root)
        queue.append(None)
        seen.add(root)

        while len(queue) > 1:
            node = queue.popleft()

            if node is None:
                numLevels += 1
                queue.append(None)
                continue

            for neighbor in node.neighbors:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)

    def bfsBidirectional(self, start, end):
        if start == end:
            return 1

        queue1, queue2 = deque(), deque()
        seen1, seen2 = set(), set()
        steps = 0

        queue1.append(start)
        seen1.add(start)
        queue2.append(end)
        seen2.add(end)

        while queue1 and queue2:
            size1, size2 = len(queue1), len(queue2)

            steps += 1
            for _ in range(size1):
                for neighbor in queue1.popleft().neighbors:
                    if neighbor in seen1:
                        continue
                    if neighbor in seen2:
                        return steps
                    queue1.append(neighbor)
                    seen1.add(neighbor)

            steps += 1
            for _ in range(size2):
                for neighbor in queue2.popleft().neighbors:
                    if neighbor in seen2:
                        continue
                    if neighbor in seen1:
                        return steps
                    queue2.append(neighbor)
                    seen2.add(neighbor)

        return -1

    def topSort(self, graph):
        order = []
        node_to_indgree = {node : 0 for node in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indgree[node] += 1

        queue = deque( [node for node in graph if node_to_indgree[node] == 0] )

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in node.neighbors:
                node_to_indgree[neighbor] -= 1
                if node_to_indgree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def binarySearch(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid
            elif num[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def binarySearchRecursive(self, nums, target):

        return self.binarySearchUtil(nums, target, 0, len(nums) - 1)

    def binarySearchUtil(self, nums, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        return self.binarySearchUtil(nums, target, mid + 1, end) if nums[mid] < target else self.binarySearchUtil(nums, target, start, mid - 1)


    def subsets(self, nums):
        nums = sorted(nums)
        subsets = []
        self.dfs(nums, 0, subset, subsets)

        return subsets
    #nums = [1,2,2], subsets = [[],[1],[1,2],[1,2],[1,2,2],[2],[2],[2,2]] [1,2,2] appear once
    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()

    def subsets2(self, nums):
        subsets = []
        nums = sorted(nums)
        self.dfs2(nums, 0, [], subsets)

        return subsets

    def dfs2(self, nums, index, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            if i > index and nums[i - 1] == nums[i]:
                continue

            subset.append(nums[i])
            self.dfs2(nums, i + 1, subset, subsets)
            subset.pop()

    def permute(self, nums):
        permutations = []
        visited = set()
        self.dfs3(nums, visited, [], permutations)
        return permutations

    def dfs3(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if i in visited:
                continue
            permutation.append(nums[i])
            visited.add(i)
            self.dfs(nums, visited, permutation, permutations)
            permutation.pop()
            visited.remove(i)

    def permuteUnique(self, nums):
        permutations = []
        visited = set()

        self.dfs4(self, sorted(nums), visited, [], permutations)
        return permutations

    def dfs4(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if i in visited or i > 0 and nums[i - 1] == nums[i] and i - 1 not in visited:
                continue
            permutation.append(nums[i])
            visited.add(i)
            self.dfs4(nums, visited, permutation, permutations)
            permutation.pop()
            visited.remove(i)

    # def partition(self, nums, k, start, end):
