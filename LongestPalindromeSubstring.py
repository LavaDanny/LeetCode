class Solution(object):
    
    def determinePalindrome(self, s):
        index = 0
        endIndex = len(s) - 1
        
        while(index < endIndex):
            if(s[index] != s[endIndex]):
                return False
            
            index += 1
            endIndex -= 1
            
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if(len(s) == 1):
            return s
        
        isPalindrome = self.determinePalindrome(s)
        if(isPalindrome == True):
            return s
        
        index = 0
        endIndex = len(s)
        size = 0
        answer = ""
        isPalindrome = False
    
        while(index < len(s)):
            
            currentLetter = s[index]
            subString = s[index:] 
            
            tracker = 0
            for x in subString:
                if(x == currentLetter and len(subString[:tracker + 1]) > size):
                    isPalindrome = self.determinePalindrome(subString[:tracker + 1])
                    
                if(isPalindrome == True):
                    size = len(subString[:tracker + 1])
                    answer = subString[:tracker + 1]
                        
                isPalindrome = False
                tracker += 1
                
            index += 1
            
            
        return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        