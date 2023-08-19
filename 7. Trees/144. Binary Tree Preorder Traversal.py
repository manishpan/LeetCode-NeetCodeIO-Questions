#Problem statement: Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
    #Preorder - Root Left Right, so we append root.val into res and stack first and then go to LST adding add nodes
    # to stack and res. Once we encounter None, we pop a Node from stack and repeat the procedure.
        if not root:
            return 
        res, stack = [], [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return res
             

    def preorderTraversalRecursive(self, root):
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