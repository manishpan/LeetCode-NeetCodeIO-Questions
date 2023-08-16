#Problem Statement: Given the head of a linked list and an integer val, remove all the nodes of the linked list that
#has Node.val == val, and return the new head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val: int):
    #We create a dummy node that will point to head of linked list. prev and curr will point to dummy and head.
        dummy = ListNode(-1, head)
        prev, curr = dummy, head

    #If the curr val is equal to val we update the next of previous to next of curr skipping the value at curr.
        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
        
        return dummy.next
    #Implementing printList fxn to print List functions
    def printList(self, head):
        while head != None:
            print(head.val, end = " ")
            head = head.next
        print()


#Testcases:
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6
head = Solution().removeElements(head, val)
Solution().printList(head)

head = None
val = 1
head = Solution().removeElements(head, val)
Solution().printList(head)

head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val = 7
head = Solution().removeElements(head, val)
Solution().printList(head)