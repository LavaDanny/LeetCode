# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        headCopy = head
        headCopy2 = head
        
        size = 0
        while(headCopy != None):
            size += 1
            headCopy = headCopy.next
            
        if(size == 1 or size == 0):
            empty = ListNode('')
            return empty
        
        else:
            newHead = head.next
            if(n == size):
                head.next = None
                return newHead
                
            else:
                place = 0
                while(place != size - n - 1):
                    head = head.next
                    place += 1
                
                temp = head
                head = head.next.next
                temp.next = head
            
                return headCopy2