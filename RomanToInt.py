# Given a roman numeral, convert it to an integer.

class Solution(object):
    
    #add or sub is 0 if subtract, 1 if add
    def processRoman(self, romanNum, hmap):
        return hmap[romanNum]
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hmap = {}
        hmap['I'] = 1
        hmap['V'] = 5
        hmap['X'] = 10
        hmap['L'] = 50
        hmap['C'] = 100
        hmap['D'] = 500
        hmap['M'] = 1000
        
        # III = 3, Iv = 4, V = 5, VI = 6, IX = 9 , X = 10, XI = 11
        # if number before is lower than the number after, subtract
        # else add
        
        ans = 0
        
        roman1 = 0
        roman2 = 0
        
        for x in range(len(s)): #x = index of s
            if (x == len(s) - 1):   #last roman numeral in string
                ans = self.processRoman(s[x], hmap) + ans
            else:
                roman1 = self.processRoman(s[x], hmap)
                roman2 = self.processRoman(s[x+1], hmap)
                if (roman1 >= roman2):
                    ans = ans + roman1
                else: 
                    ans = ans - roman1
                    
        return ans