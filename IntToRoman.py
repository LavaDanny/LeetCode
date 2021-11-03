class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # special cases: 4 9 40 90 400 900
        # 1994 "MCMXCIV"
        
        # special if:
        # first digit is 4 or 9
        # second digit is 4 or 9
        # third digit is 4 or 9
        
        number = str(num)
        
        answer = ""
        
        length = len(number)
        arr = []
        
        for c in number:
            arr.append(c)
        
        for x in arr:
            print(x)
            
            if(length == 4):
                for y in range(int(x)):
                    answer = answer + "M"
                    
                length -= 1
                
            if(length == 3):
                
                digit3 = arr[-3]
                
                if(digit3 == "9"):
                    answer = answer + "CM"
                elif(digit3 == "4"):
                    answer = answer + "CD"
                else:
                    
                    digit3 = int(digit3)
                    if digit3 >= 5:
                        answer = answer + "D"
                        digit3 -= 5
                    if digit3 > 0:
                        for z in range(digit3):
                            answer = answer + "C"
                    
                length -= 1
            
            if(length == 2):
                
                digit3 = arr[-2]
                
                if(digit3 == "9"):
                    answer = answer + "XC"
                elif(digit3 == "4"):
                    answer = answer + "XL"
                else:
                    digit3 = int(digit3)
                    if digit3 >= 5:
                        answer = answer + "L"
                        digit3 -= 5
                    if digit3 > 0:
                        for a in range(digit3):
                            answer = answer + "X"
                    
                length -= 1
                      
                    
            if(length == 1):
                
                digit4 = arr[-1]
                
                if(digit4 == "9"):
                    answer = answer + "IX"
                elif(digit4 == "4"):
                    answer = answer + "IV"
                else:
                    digit4 = int(digit4)
                    if digit4 >= 5:
                        answer = answer + "V"
                        digit4 -= 5
                    if digit4 > 0:
                        for b in range(digit4):
                            answer = answer + "I"
                    
                length -= 1
                
                
            return answer