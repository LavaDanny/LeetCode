class Solution {
public:
    bool isAnagram(string s, string t) {
        int sArr[128] = {0};
        int tArr[128] = {0};
        
        for(int i = 0; i < s.size(); i++){
            sArr[int(s[i])]++;
        }
        
        for(int i = 0; i < t.size(); i++){
            tArr[int(t[i])]++;
        }
        
        for(int i = 0; i< 128; i++){
            if(tArr[i] != sArr[i]){
                return false;
            }
        }
        
        return true;
    }
};