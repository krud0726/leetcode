class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for i, v in enumerate(matrix):
            if target in v:
                return True
            
        return False

    
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            
        return False
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in row for row in matrix])
        