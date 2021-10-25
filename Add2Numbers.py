# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def list_sum(item, sum):
    
    if item == None:
        return sum
    
    sum = sum * 10
    sum = sum + item.val
    return list_sum(item.next, sum)

def reverse_num(num, zeroes):
    temp = 0
    while num > 0:
        temp = temp * 10 + num % 10
        num = num / 10
        
    while(zeroes > 0):
        temp *= 10
        zeroes -= 1
        
    return temp
    
def create_list(ans, num):
    
    if num == 0:
        return ans
    
    ans2 = ListNode(num % 10)
    ans.next = ans2
    return create_list(ans2, num / 10)
    

class Solution(object):
        
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        check1 = 0
        temp1 = l1
        zeroes1 = 0
        
        check2 = 0
        temp2 = l2
        zeroes2 = 0
        
        while(check1 == 0 and temp1 != None):
            if(temp1.val == 0):
                temp1 = temp1.next
                zeroes1 += 1
            else:
                check1 = 1
                
        while(check2 == 0 and temp2 != None):
            if(temp2.val == 0):
                temp2 = temp2.next
                zeroes2 += 1
            else:
                check2 = 1
        
        l1sumRev = list_sum(l1, 0)
        l2sumRev = list_sum(l2, 0)
        
        l1sum = reverse_num(l1sumRev, zeroes1)
        l2sum = reverse_num(l2sumRev, zeroes2)
        
        ansSum = l1sum + l2sum
        
        ans = ListNode(ansSum % 10)
        
        create_list(ans, ansSum / 10)
        
        return ans
        

        
        