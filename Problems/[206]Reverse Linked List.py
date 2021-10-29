# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = []
        node = head
        while node:
            nodes.append(node)
            if node.next:
                node = node.next
            else:
                break
        for item in nodes:
            item.next = None
        head = nodes.pop(-1)
        node = head
        while nodes:
            node.next = nodes.pop(-1)

            node = node.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
