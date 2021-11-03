class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        smallest = 201
        word = ""
        
        for x in strs:
            if x == "":
                return ""
            
            if len(x) < smallest:
                smallest = len(x)
                word = x
            
        if len(strs) == 1:
            return strs[0]
        
        
        same = True
        index = 0
        currentLetter = word[0]
        answer = ""
        while(same == True):
            for x in strs:
                if(x[index] != currentLetter):
                    same = False
                    
            if(same == True):
                answer = answer + x[index]
                if(index + 1 != len(word)):
                    index += 1
                else:
                    same = False
                currentLetter = word[index]
                
        return answer
        