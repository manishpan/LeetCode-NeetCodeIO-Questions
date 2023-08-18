#Problem statement: Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
    #We create a list res, that will store the value in preorder traversal fashion.
        res = []

    #Defining a function to implement recursive implementation of Preorder traversal
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return res

#Testcases:
root = [1,None,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().preorderTraversal(root))

root = TreeNode()
print(Solution().preorderTraversal(root))

root = TreeNode(1)
print(Solution().preorderTraversal(root))