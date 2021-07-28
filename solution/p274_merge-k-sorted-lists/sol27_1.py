# https://leetcode.com/problems/merge-k-sorted-lists

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode()
        heap = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        while heap:
            (_, idx, node) = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            result.next = node
            result = result.next

        return root.next
