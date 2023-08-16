#Problem Statement: Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
    #We initialize two pointers fast and slow both at the head of linked list.
        fast, slow = head, head

    #The fast pointers will move 2 steps at a time while slow pointers will move 1 step. By the time, fast move to
    #last node or goes out of bound, the slow will be at the middle of the linked list. We return slow pointer.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow  
    
    #Implementing printList function to print Linked List
    def printList(self, head):
        while head:
            print(head.val, end = " ")
            head = head.next
        print()

#Testcases:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = Solution().middleNode(head)
Solution().printList(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
head = Solution().middleNode(head)
Solution().printList(head)