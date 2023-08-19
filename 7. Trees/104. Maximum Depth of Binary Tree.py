#Problem Statement: Given the root of a binary tree, return its maximum depth.

#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
#leaf node.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthBFS(self, root) -> int:
    #The level of tree is equal to maxDepth of the tree, so we maintain a level variable and implement BFS.
        if not root:
            return 0
        
        level = 0
        q = deque(([root]))

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            level += 1
        
        return level

    def maxDepthIterativeDFS(self, root) -> int:
    #We store a node and its depth in stack. For if we add the children of a node, we add its depth by increment 1.
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return res

    def maxDepthRecursiveDFS(self, root) -> int:
        if not root:
            return 0
        lst = self.maxDepthRecursiveDFS(root.left)
        rst = self.maxDepthRecursiveDFS(root.right)
        return 1 + max(lst, rst)
    
#Testcases:
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxDepthRecursiveDFS(root))

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxDepthIterativeDFS(root))
      
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxDepthBFS(root))