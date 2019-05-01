from graph.tree import Node


class BinaryTree :

    def shortestDistance(self, root: Node, node1: Node, node2: Node) -> int :




    def getLowestCommonAncestor(self, node: Node, node1: Node, node2: Node) -> Node :

        if node == node1 or node == node2:
            return node

        left = right = None

        if node.left :
            left =
