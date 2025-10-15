# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=float('-inf')
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left_max=max(0,dfs(node.left))
            right_max=max(0,dfs(node.right))
            result=max(result,node.val+left_max+right_max)# with split
            return node.val+max(left_max,right_max) # without split passed to parents
        dfs(root)
        return result
        
        
        
        

        