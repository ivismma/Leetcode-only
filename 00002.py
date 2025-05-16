# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseNumber(l1: Optional[ListNode], l2: Optional[ListNode], i):
    if l1 != None:
        if l2 != None: # soma l1 e l2
            return l1.val*10**i + l2.val*10**i + reverseNumber(l1.next, l2.next, i+1)
        else: #soma só l1
            return l1.val*10**i + reverseNumber(l1.next, None, i+1)
    elif l2 != None: # soma só l2
        return l2.val*10**i + reverseNumber(None, l2.next, i+1)
    
    return 0

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = reverseNumber(l1, l2, 0)

        # passa dígitos pra lista:
        reversedList = ListNode(total%10)
        currentNode = reversedList
        total //= 10
        while total != 0:
            currentNode.next = ListNode(total%10)
            currentNode = currentNode.next
            total //= 10
        
        return reversedList
