from list import Node


class Traverse :

    def reverseIterative(self, head: Node) -> Node :
        prv = None
        cur = head

        while cur :
            nxt = cur.next

            cur.next = prv

            prv = cur
            cur = nxt

        return prv

    def reverseRecursive(self, node: Node) -> Node :

        if node is None or node.next is None :
            return node

        head = self.reverseRecursive(node.next)

        node.next.next = node
        node.next = None

        return head

