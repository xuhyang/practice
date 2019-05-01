from graph.tree import Node


class BST :

    def shortestDistanceBetween(self, node1, node2, root: Node) -> int :
        lca = self.getLowestCommonAncestor(root, node1, node2)
        return self.distanceBetween(lca, node1) + self.distanceBetween(lca, node2)

    def getLowestCommonAncestor(self, node: Node, node1: Node, node2: Node) -> Node :

        while True :
            if node.val < node1.val and node.val < node2.val :
                node = node.right
            elif node.val > node1.val and node.val > node2.val :
                node = node.left
            else :
                return node

    def distanceBetween(self, ancestor: Node, val: int) -> int :
        distance = 0
        node = ancestor

        while True :
            if node.val == val :
                return distance
            elif node.val > val :
                node = node.left
            else :
                node = node .right
            distance += 1

