# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, l1 : ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge2Lists(l1.next ,l2)
            
        return l1 or l2
    
    
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        # using runner trick
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        
        # 병합 정렬을 위해 중간 지점에서 요소들 자르기
        half.next = None
        
        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        return self.merge2Lists(l1, l2)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        
        while p:
            lst.append(p.val)
            p = p.next
            
        # 정렬
        lst.sort()
        
        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in lst:
            p.val = i
            p = p.next
            
        return head
        