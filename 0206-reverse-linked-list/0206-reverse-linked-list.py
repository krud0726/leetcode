# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        list_node = []
        
        while node:
            list_node.append(node.val)
            node = node.next
        
        list_node.reverse()
        node = head
        
        for i in list_node:
            node.val = i
            node = node.next
            
            
        return head
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        node = head
        
        list_node = []
        
        while node:
            temp = node
            node = node.next
            temp.next = before
            before = temp
        
        return before
        