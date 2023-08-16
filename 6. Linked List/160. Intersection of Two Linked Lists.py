#Problem Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two
#lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNodeOptimal(self, headA, headB):
    #Creating temporary pointers.
        l1, l2 = headA, headB

    # We let both pointers run till null, if they become null we assign headB to l1 and headA to l2.
    # We keep on doing so unless l1 and l2 are different, once they are same we return l1.
        while l1 != l2:
            if l1:  l1 = l1.next
            else:   l1 = headB
            
            if l2:  l2 = l2.next
            else:   l2 = headA
        
        return l1

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
    #This code requires some helper function to calculate length of linked list and to skip lenDiff part of Linked List.
    # We first calculate the length of two LLs and the difference between their length.
        lenA, lenB = self.lengthList(headA), self.lengthList(headB)

        lenDiff = abs(lenA - lenB)

    #Based on lenDiff, we skip the lenDiff nodes in the longer LLs.
        if lenA > lenB: headA = self.skip(headA, lenDiff)
        elif lenA < lenB:   headB = self.skip(headB, lenDiff)
    
    #Now we simple check if the node in both the list is same or not and we return node or None accordingly.
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

    def lengthList(self, head) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def skip(self, head, lenDiff):
        while lenDiff > 0:
            head = head.next
            lenDiff -= 1
        return head

    def printList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print("")

#Testcases:
headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
headB = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))
intersect = Solution().getIntersectionNodeOptimal(headA, headB)
Solution().printList(intersect)

headA = ListNode(1, ListNode(9, ListNode(1, ListNode(2, ListNode(4)))))
headB = ListNode(3, ListNode(2, ListNode(4)))
intersect = Solution().getIntersectionNodeOptimal(headA, headB)
Solution().printList(intersect)

headA = ListNode(2, ListNode(6, ListNode(4)))
headB = ListNode(1, ListNode(5))
intersect = Solution().getIntersectionNodeOptimal(headA, headB)
Solution().printList(intersect)