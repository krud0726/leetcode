class MyCircularDeque1:
    def __init__(self, k: int):
        self.count = 0
        self.k = k
        self.f = []
        self.r = []

    def insertFront(self, value: int) -> bool:
        if self.count < self.k:
            self.f.append(value)
            self.count += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.k:
            self.r.append(value)
            self.count +=1 
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.count != 0:
            if self.f:
                self.f.pop()
            elif self.r:
                self.r.pop(0)
            self.count -= 1
            return True
        
        else:
            return False

    def deleteLast(self) -> bool:
        if self.count != 0:
            if self.r:
                self.r.pop()
            elif self.f:
                self.f.pop(0)
            self.count -= 1
            return True
        else:
            return False
                

    def getFront(self) -> int:
        if self.f:
            return self.f[-1]
        elif self.r:
            return self.r[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.r:
            return self.r[-1]
        elif self.f:
            return self.f[0]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        else:
            return False
        

class ListNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.count = 0
        self.head.right, self.tail.left = self.tail, self.head
        
    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        temp = node.right
        node.right = new
        new.left, new.right = node, temp
        temp.left = new
        
    def _del(self, node: ListNode):
        temp = node.right.right
        node.right = temp
        temp.left = node
    
    # 기존의 head와 tail의 노드들은 놔두고 head와 tail 사이에 노드들을 집어넣는 방식
    def insertFront(self, value: int) -> bool:
        if self.count == self.k:
            return False
        self.count += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.k:
            return False
        self.count += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1
        self._del(self.tail.left.left)
        return True
        
    def getFront(self) -> int:
        return self.head.right.val if self.count else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.count else -1
        
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()