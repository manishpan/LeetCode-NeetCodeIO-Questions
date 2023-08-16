#Problem Statement: You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
#lists.

#Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
    #We create a dummy node head and a pointer curr. We compare value of list1 and list2 and whichever is smaller
    # we add it to dummy node and updating the concern pointer.
        head = ListNode(0)
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:   curr.next = list1
        elif list2: curr.next = list2

        return head.next
    
    #Implementing a print list function.
    def printList(self, head):
        while head != None:
            print(head.val, end = " ")
            head = head.next
        print("")

#Testcases:
list1 = ListNode(1, ListNode(2, ListNode(4)))   #List1 : 1 -> 2 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))   #List2 : 1 -> 3 -> 4
head = Solution().mergeTwoLists(list1, list2)
Solution().printList(head)

list1 = None
list2 = None
head = Solution().mergeTwoLists(list1, list2)
Solution().printList(head)

list1 = None            #List1 : 
list2 = ListNode(0)     #List2 : 0
head = Solution().mergeTwoLists(list1, list2)
Solution().printList(head)