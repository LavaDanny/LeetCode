# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
            
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        characters = [0] * 128
        greatestLength = 0
        index = 0
        stringLength = len(s)
        length = 0
        
        
        for x in range(stringLength):
            if(characters[ord(s[x])] == 1):
                
                if(length > greatestLength):
                    greatestLength = length
                index = x - 1
                
                characters = [0] * 128
                characters[ord(s[x])] += 1
                length = 0
                
                while(characters[ord(s[x])] == 1):
                    characters[ord(s[index])] += 1    
                    index -= 1
                    length += 1
                
                characters[ord(s[x])] -= 1
                
            else: 
                characters[ord(s[x])] += 1
                length += 1
                          
        if(length > greatestLength):
            greatestLength = length
                
        return greatestLength
            