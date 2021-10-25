# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.




class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        degrees = {}
        
        #find degree of each element
        for x in nums:
            if(x in degrees):
                degrees[x] += 1
            else:
                degrees[x] = 1

        #find maximim degree
        maximumDegree = 0
        for key in degrees:
            if(degrees[key] > maximumDegree):
                maximumDegree = degrees[key]
            
        #get numbers with max freq
        maxDegreesArr = []    
        for key in degrees:
            if(degrees[key] == maximumDegree):
                maxDegreesArr.append(key)
            
        
        subArrSize = []    
        #find size of subarray with max degrees
        for degree in maxDegreesArr:
            count = 0
            beginCount = 0
            end = 0
            
            for x in nums:
                
                if(x == degree):
                    beginCount = 1
                    end += 1
                    
                if(beginCount == 1):
                    count += 1
                    
                if(end == maximumDegree):
                    break
                      
            #save size of subarray in count
            subArrSize.append(count)
            
        return(min(subArrSize))
                    
        
            