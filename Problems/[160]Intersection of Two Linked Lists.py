# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA and headB:
            stackA = self.nodeToStack(headA)
            stackB = self.nodeToStack(headB)
            intersect = 0

            while stackA and stackB:
                topA = stackA.pop()
                topB = stackB.pop()
                if topA != topB:
                    if intersect == 0:
                        return None
                    else:
                        return prev
                else:
                    intersect += 1
                    prev = topA

            return prev

        else:
            return None

        def nodeToStack(self, head: ListNode):
            nodeStack = []
            while head:
                nodeStack.append(head)
                head = head.next

            return nodeStack
# leetcode submit region end(Prohibit modification and deletion)
