class Traverse :

    def bfs(self, graph, root) :
        queue = []
        visited = set()

        queue.append(root)
        visited.add(root)

        while queue :
            node = queue.pop(0)

            for neighbor in graph[node] :
                if neighbor not in visited :
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfsIterative(self, graph, root):
        stack = []
        visited = set()

        stack.append(root)

        while stack :
            node = stack.pop()
            visited.add(root)

            for neighbor in graph(node) :
                if neighbor not in visited :
                    stack.append(neighbor)

    def dfsRecursive(self, graph, node) :
        visited = set()

        self.dfsUtil(graph, node, visited)

    def dfsUtil(self, graph, node, visited) :
        visited.add(node)

        for neighbor in graph[node] :
            if neighbor not in visited :
                self.dfsUtil(graph, neighbor, visited)

    def topSort(self, graph) :
        visited = set()
        result = []

        for node in graph.keys() :
            if node not in visited :
                self.topSortUtil(node, graph, visited, result)

    def topSortUtil(self, node, graph, visited, result) :
        visited.add(node)

        for neighbor in graph[node] :
            if neighbor not in visited :
                self.topSortUtil(neighbor, graph, visited, result)

        result.insert(0, node)

    def bfsWithDepth(self, graph, root) :
        queue = []
        visited = set()
        depth = 0

        queue.append(root)
        queue.append(None)

        visited.add(root)

        while queue :
            node = queue.pop(0)
            if node is None :
                depth += 1
                continue

            for neighbor in graph[node] :
                if neighbor not in visited :
                    queue.append(neighbor)
                    visited.add(neighbor)
            queue.append(None)

    def bfsWithDepth2(self, graph, root) :
        queue = []
        marked = set()
        marked.add(root)
        queue.append((root, 0))

        depth = 0
        while queue :
            r, d = queue.pop(0)
            if d > depth :  # increase depth only when you encounter the first node in the next depth
                depth += 1
            for node in graph[r] :
                if node not in marked :
                    marked.add(node)
                    queue.append((node, depth + 1))