# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        while head is not None and head.next is not None and head.val == head.next.val:
            while slow.next is not None:
                if slow.next.val != head.val:
                    head = slow.next
                    slow = head
                    break
                elif slow.next.next is None:
                    return None
                slow = slow.next

        slow = head
        while slow is not None and slow.next is not None:
            fast = slow.next
            while fast.next is not None:
                if fast.next.val == fast.val:
                    if fast.next.next is not None:
                        fast.next = fast.next.next
                    else:
                        slow.next = None
                        return head
                    if slow.next.next is not None:
                        slow.next = slow.next.next
                    else:
                        slow.next = None
                else:
                    break
            if slow.next.next is None or (slow.next.next is not None and slow.next.next.val != slow.next.val):
                slow = slow.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
