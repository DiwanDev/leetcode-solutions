

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        k, j = 0, len(nodes) - 1
        while k < j:
            nodes[k].next = nodes[j]
            k += 1
            if k >= j:
                break
            nodes[j].next = nodes[k]
            j -= 1

        nodes[k].next = None