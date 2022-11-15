# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = list1
        h2 = list2
        record = []
        
        cur = None
        before = None
        
        while h1 and h2:
            
            if h1.val > h2.val:
                cur = h2
                h2 = h2.next
                cur.next = h1
                record.append(2)
                
            else:
                cur = h1
                h1 = h1.next
                cur.next = h2
                record.append(1)
                
            if before:
                before.next = cur
                
            before = cur
            
        if record and record[0] == 1:
            answer = list1
        elif record and record[0] == 2:
            answer = list2
        else:
            if list1 and not list2:
                answer = list1
            else:
                answer = list2
                
                
        return answer
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
            
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
            
        return list1
        