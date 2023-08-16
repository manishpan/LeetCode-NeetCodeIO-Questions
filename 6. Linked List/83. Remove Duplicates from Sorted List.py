#Problem Statement: Given the head of a sorted linked list, delete all duplicates such that each element appears only
#once. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
    #Using a pointer curr to traverse the linked list
        curr = head

    #We keep on removing the nodes for which curr.val == curr.next.val and when we find a different node, we set
    # curr to be next of curr.
        while curr.next and curr.next.val == curr.val:
            curr.next= curr.next.next
        curr = curr.next

        return head

    #Implementing printList to print Linked List
    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

#Testcases:
head = ListNode(1, ListNode(1, ListNode(2)))
head = Solution().deleteDuplicates(head)
Solution().printList(head)

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
head = Solution().deleteDuplicates(head)
Solution().printList(head)