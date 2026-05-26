# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point_1, point_2 = head, head

        while point_1 and point_1.next:
            point_2 = point_2.next
            point_1 = point_1.next.next
            if point_2==point_1:
                return True
        return False
            