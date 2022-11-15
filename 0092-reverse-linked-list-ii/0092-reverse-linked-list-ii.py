# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        count = 1
        position = head
        reverse_start = None
        
        reverse = []
        
        while position:
            
            if count == left:
                reverse_start = position
            
            if (count >= left and count <= right):
                reverse.append(position.val)
            
            position = position.next
            count += 1
            
        reverse.reverse()
        print(reverse)
        
        for i in reverse:
            reverse_start.val = i
            reverse_start = reverse_start.next
        
        return head
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        # start, end 위치 선정 - 정해진 위치로의 이동
        for _ in range(left-1):
            start = start.next
            
        end = start.next
        
        # 반복 과정을 통해 m,n 사이의 노드를 역순으로 뒤집기
        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            
            
        return root.next
        