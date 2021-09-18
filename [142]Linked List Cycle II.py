# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        seen = []
        node = head
        pos = 0
        while node:
            if node.next is None:
                return None
            if node in seen:
                return node
            seen.append(node)
            node = node.next
# leetcode submit region end(Prohibit modification and deletion)
