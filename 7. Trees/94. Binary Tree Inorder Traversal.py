#Problem Statement: Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
    #If root is empty we return None.
        if root == None:
            return None
    
    #res will store the result of our inorder traversal while stack will be used to store the addresses of root
    # nodes.
        res = []
        stack = []
        curr = root

    #We keep on traversing left till we encounter None, storing root nodes in stack data.
        while curr != None:
            stack.append(curr)
            curr = curr.left

    #Once we reach None, we pop the last inserted Node in stack, add it to res list and go to root.right
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            while curr != None:
                stack.append(curr)
                curr = curr.left
        
        return res

    def inorderTraversalRecursive(self, root):
    #In order to store result in a list named res, we will need to either declare res outside a function.
    #In order to make the recursive function, we write a recursive function within the function inorderTraversal.
        res = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res
    
#Testcases:
root = [1,None,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().inorderTraversal(root))

root = TreeNode()
print(Solution().inorderTraversal(root))

root = TreeNode(1)
print(Solution().inorderTraversal(root))