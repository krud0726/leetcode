import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # BFS
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def bfs(root, a):
            
            q = collections.deque([])
            q.append(root)
            
            while q:
                temp = q.popleft()
                
                if not temp:
                    a.append(0)
                    continue
                
                a.append(temp.val)
                    
                q.append(temp.left)
                q.append(temp.right)
            print(a)
            return a
            
        return bfs(p, []) == bfs(q, [])

    
    # Recursive
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def recursive(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and recursive(p.left, q.left) and recursive(p.right, q.right)
            
        return recursive(p,q)
            

    
    # DFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p,q):
            stack = [(p,q)]
            
            while stack:
                v1, v2 = stack.pop()
                
                if not v1 and not v2:
                    pass
                elif not v1 or not v2:
                    return False
                else:
                    if v1.val != v2.val: return False
                    stack.append((v1.left, v2.left))
                    stack.append((v1.right, v2.right))
                    
            return True
        
        return dfs(p,q)
        
                
                
    