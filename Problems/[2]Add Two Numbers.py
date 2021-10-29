# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = []
        val2 = []
        self.post(l1, val1)
        self.post(l2, val2)
        val = list(str(int("".join(val1)) + int("".join(val2))))
        val.reverse()
        root = ListNode(int(val[0]))
        head = root
        if len(val) == 1:
            return root
        for i in range(1, len(val)):
            head.next = ListNode(int(val[i]))
            head = head.next
        return root

    def post(self, root, val):
        if root is None:
            return
        self.post(root.next, val)
        val.append(str(root.val))
# leetcode submit region end(Prohibit modification and deletion)
