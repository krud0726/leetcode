class MyStack:

    def __init__(self):
        self.stk = collections.deque()

    def push(self, x: int) -> None:
        self.stk.append(x)
        
        for _ in range(len(self.stk) - 1):
            self.stk.append(self.stk.popleft())
            
    def pop(self) -> int:
        return self.stk.popleft()

    def top(self) -> int:
        return self.stk[0]

    def empty(self) -> bool:
        return not self.stk
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()