# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        track = []
        
        def Inorder(r):
            
            if not r:
                return
            
            Inorder(r.left)
            track.append((r.val, r))
            Inorder(r.right)
            
        Inorder(root)
        # 리스트를 자체적으로 정렬 시키는 것은 .sort()
        # 정렬된 리스트를 반환하는 것은 sorted()
        target = sorted(track)
        
        for i in range(len(track)):
            pos_cur, pos_sol = track[i][1], target[i][1]
            
            if track[i] != target[i]:
                pos_cur.val, pos_sol.val = pos_sol.val, pos_cur.val
                break
                
            
        
        