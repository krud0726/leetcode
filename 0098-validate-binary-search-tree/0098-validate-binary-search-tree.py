# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r, left, right):
            if r:
                if r.val <= left or r.val >= right: return False
                return dfs(r.left, left, r.val) and dfs(r.right, r.val, right)
            
            return True
        
        return dfs(root, -float('inf'), float('inf'))
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        s = [(root, -float('inf'), float('inf'))]
        
        while s:
            node, left, right = s.pop()
            if node.val <= left or node.val >= right: return False
            if node.left: s.append((node.left, left, node.val))
            if node.right: s.append((node.right, node.val, right))
        return True
                