# https://leetcode.com/problems/merge-two-sorted-lists

class ListNode:
    def __init__(self, val=0, *vals):
        self.val = val
        self.next = None
        for value in vals:
            self.add(value)

    def add(self, val):
        if not self.next:
            self.next = type(self)(val)
            return
        node = self.next
        while node.next:
            node = node.next
        node.next = type(self)(val)

    def __str__(self):
        s = "\n"
        node = self
        while node:
            s += str(node.val) + " "
            node = node.next
        return s

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1



sol = Solution()
l1 = ListNode(1, 2, 4)
print(l1)
l2 = ListNode(1, 3, 4)
print(l2)


answer = sol.mergeTwoLists(l1, l2)
print(answer)
