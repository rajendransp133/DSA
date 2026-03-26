# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def recursion(node,maxx):
            nonlocal count
            if(node.left):
                if(node.left.val>=maxx):
                    count+=1
                    curr_left_max=node.left.val                        
                    recursion(node.left,curr_left_max)
                else:
                    recursion(node.left,maxx)
            if(node.right):
                if(node.right.val>=maxx):
                    count+=1
                    curr_right_max=node.right.val  
                    recursion(node.right,curr_right_max)
                else:
                    recursion(node.right,maxx)


        recursion(root,root.val)
        return count+1
