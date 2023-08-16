#Problem statement: Given the head of a singly linked list, return true if it is a palindrome  or false otherwise.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
    #We first find the middle of Linked List using fast and slow pointers. The slow pointer will point to middle of 
    #list.
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

    #We reverse the list from the point slow pointer is pointing.
        revHead = self.reverseList(slow)

    #We compare head and revHead until head points to the same node as pointed by slow.
        while head != slow:
            if head.val != revHead.val:
                return False
            head = head.next
            revHead = revHead.next
        
        return True

    def reverseList(self, head, prev=None):
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
    
#Testcases:
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(Solution().isPalindrome(head))

head = ListNode(1, ListNode(2))
print(Solution().isPalindrome(head))