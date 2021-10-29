# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        cycle = ListNode("here")
        while head:
            if head.val == "here":
                return True
            t = head
            head = t.next
            t.next = cycle
        return False
# leetcode submit region end(Prohibit modification and deletion)
