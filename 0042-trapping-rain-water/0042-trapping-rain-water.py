class Solution:
    def trap2(self, height: List[int]) -> int:
        trap = 0
        
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
                
            if left_max <= right_max :
                trap += left_max - height[left]
                left += 1
            else:
                trap += right_max - height[right]
                right -= 1
                
        return trap
    
    
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()
                
                if not len(stack):
                    break
                    
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
            
        return volume
        