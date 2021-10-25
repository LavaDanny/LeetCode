# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        if(len(s) % 2 == 1):
            return False
        
        for x in s:
            
            if((x == ']' or x == '}' or x == ')') and not stack):
                return False
            
            if(x == '(' or x == '{' or x == '['):
                stack.append(x)
            elif(x == ')'):
                if(stack[-1] != '('):
                    return False
                else:
                    stack.pop()
            elif(x == '}'):
                if(stack[-1] != '{'):
                    return False
                else:
                    stack.pop()
            elif(x == ']'):
                if(stack[-1] != '['):
                    return False
                else:
                    stack.pop()
                
        if(not stack):
            return True
        else:
            return False
                
            
        