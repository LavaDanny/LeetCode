class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x == 0):
            return 0
        
        y = str(x)
        
        # check if negative
        if(y[0] == '-'):
            negative = 1
            y = y[1:]
        else:
            negative = 0
        
        while(y[-1] == '0'):
            y = y[:len(y) - 1]
        
        left = 0
        right = len(y) - 1
        
        answer = ""
        
        # even number of digits
        if((len(y) - 1) % 2 == 0):
            answer = y[(len(y) - 1) / 2] 
            right = ((len(y) - 1) / 2) + 1
            left = ((len(y) - 1) / 2) - 1
            
        # odd number of digits    
        else:
            right = (len(y) / 2)
            left = (len(y) / 2) - 1
        
        # start swapping digit positions
        while(right < len(y) and left >= 0):
            answer = answer + y[left]
            answer = y[right] + answer
            
            left -= 1
            right += 1
            
        x = int(answer)
        
        # make negative if necessary
        if(negative == 1):
            x *= -1
            
        # check if outside 32bit int range
        if(x > 2**31 - 1):
            return 0
        if(x < -2**31):
            return 0
        
        return x
        
        