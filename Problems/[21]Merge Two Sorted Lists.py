# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = []
        val2 = []
        self.traverse(l1, val1)
        self.traverse(l2, val2)
        for i in val2:
            val1.append(i)
        val1.sort()
        if len(val1) == 0:
            return None
        new = ListNode(val1[0])
        pointer = new
        for i in range(1, len(val1)):
            pointer.next = ListNode(val1[i])
            pointer = pointer.next
        return new

    def traverse(self, root, val):
        if root is None:
            return
        val.append(root.val)
        self.traverse(root.next, val)
# leetcode submit region end(Prohibit modification and deletion)
