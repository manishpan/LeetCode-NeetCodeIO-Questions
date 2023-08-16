#Problem Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
#following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
#connected to. Note that pos is not passed as a parameter.

#Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
    #We will use fast and slow pointers technique. fast pointer will move 2 times as fast as slow pointer.
    # We could have used hashSet and store the nodes in the set. If we encounter a node that is already in hashSet
    # that means there is a cycle and we return True.
        fast, slow = head, head

    # If there is a cycle, the fast and slow pointer will eventually meet. If there is no cycle, the fast pointer
    # will become None and we come out of loop normally and return False.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

#Testcases:
head = ListNode(3)
head.next = ListNode(2, ListNode(0, ListNode(-4, head)))
print(Solution().hasCycle(head))

head = ListNode(1)
head.next = ListNode(2, head)
print(Solution().hasCycle(head))

head = ListNode(1)
print(Solution().hasCycle(head))