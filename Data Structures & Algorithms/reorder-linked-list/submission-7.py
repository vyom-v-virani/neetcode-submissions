# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        list1 = []
        curr = head
        
        while curr:
            list1.append(curr)
            curr = curr.next
        

        list2 = []
        left = 0
        right = len(list1)-1
        while len(list2) < len(list1):
            list2.append(list1[left])
            left += 1
            if len(list2) < len(list1):
                list2.append(list1[right])
                right -= 1
        
        for i in range(len(list2) - 1):
            list2[i].next = list2[i+1]
        list2[-1].next = None
        return