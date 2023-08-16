#Problem statement: Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Iterative Solution
    def reverseList(self, head, prev = None):
        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
    
    #Recursive Solution
    def recReverseList(self, head, prev=None):
        if head == None:
            return prev
        
        nxt = head.next
        head.next = prev
        return self.recReverseList(nxt, head)

    #implementing printList fxn to print list
    def printList(self, head):
        while head != None:
            print(head.val, end =" ")
            head = head.next
        print()

#Testcases:
head = ListNode(1)
head.next = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))  #List is 1 -> 2 -> 3 -> 4 -> 5
head = Solution().reverseList(head)     #iterative function
Solution().printList(head)  #Output is 5 -> 4 -> 3 -> 2 -> 1
head = Solution().recReverseList(head)  #Recursive function
Solution().printList(head)  #Output is 1 -> 2 -> 3 -> 4 -> 5


head = ListNode(1, ListNode(2))     #List is 1 -> 2
head = Solution().reverseList(head) #Iterative function
Solution().printList(head)          #2 -> 1
head = Solution().recReverseList(head)  #Recursive function
Solution().printList(head)  #Output is 1 -> 2

head = None                     #List is empty
head = Solution().reverseList(head)
Solution().printList(head)
head = Solution().recReverseList(head)  #Recursive function
Solution().printList(head)  