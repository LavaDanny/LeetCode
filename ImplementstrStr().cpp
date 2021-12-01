class Solution {
public:
    int strStr(string haystack, string needle) {
        
        if(needle == haystack){
            return 0;
        }
        
        if(needle == ""){
            return 0;
        }
        
        if(needle.size() > haystack.size()){
            return -1;
        }
        
        int needleIndex = 0;
        int needleSize = needle.size();
        
        for(int i = 0; i < haystack.size(); i++){
            
            if(needle[needleIndex] == haystack[i]){
                needleIndex++;
            }
            else{
                i -= needleIndex;
                needleIndex = 0;
            }
            
            
            if(needleIndex == needleSize){
                return i - needleSize + 1;
            }
        }
        
        return -1;
        
    }
};