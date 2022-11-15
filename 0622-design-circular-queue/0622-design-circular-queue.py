class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k+1
        self.front = 0
        self.rear = 0
        self.q = [None]*(k+1)

    def enQueue(self, value: int) -> bool:
        if self.front == ((self.rear+1)%self.size):
            return False
        
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if (self.front) == self.rear:
            return False
        
        self.front = (self.front + 1) % self.size
        self.q[self.front] = None
        
        return True

    def Front(self) -> int:
        if self.front == self.rear:
            return -1
        
        return self.q[(self.front+1)%self.size]

    # 공백과 포화 상태를 구별하기 위해서 front의 내용은 비워놓는다.
    def Rear(self) -> int:
        print("self.rear : ", self.rear)
        print("self.front : ", self.front)
        if self.front == self.rear:
            return -1
        
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front == ((self.rear+1)%self.size)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()