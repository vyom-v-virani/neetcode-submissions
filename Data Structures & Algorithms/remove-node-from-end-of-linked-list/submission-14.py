class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1 = []
        prev, curr = None, head
        while curr:
            list1.append(curr)
            curr = curr.next
        
        # Remove the node at the calculated index
        list1.pop(len(list1) - n)
        
        if not list1:
            return None
            
        for i in range(len(list1) - 1):
            list1[i].next = list1[i+1]
        list1[-1].next = None
        return list1[0]