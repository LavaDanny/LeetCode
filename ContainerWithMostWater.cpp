class Solution {
public:
    int maxArea(vector<int>& height) {
        
//         int lowerHeight = 0;
//         int volume = 0;
//         int maxVolume = 0;
        
//         for(int i = 0; i < height.size(); i++){
            
//             volume = 0;
//             int length = 1;
//             for(int j = i + 1; j < height.size(); j++){
//                 if(height[i] < height[j]){
//                     lowerHeight = height[i];
//                 }
//                 else{
//                     lowerHeight = height[j];
//                 }
                
//                 volume = lowerHeight * length;
//                 if(volume > maxVolume){
//                     maxVolume = volume;
//                 }
                
//                 length++;
                
//             }
//         }
        
        int lowerHeight = 0;
        int volume = 0;
        int maxVolume = 0;
        
        int left = 0;
        int right = height.size() - 1;
        
        int maxHeightLeft = 0;
        int maxLeftIndex = 0;
        
        int maxHeightRight = 0;
        int maxRightIndex = height.size() - 1;
        
        while(left < right){
            
            if(height[left] > maxHeightLeft || height[right] > maxHeightRight){

                if(height[left] > maxHeightLeft){
                    maxHeightLeft = height[left];
                    maxLeftIndex = left;
                }
                
                if(height[right] > maxHeightRight){
                    maxHeightRight = height[right];
                    maxRightIndex = right;
                }
                
                if(maxHeightLeft < maxHeightRight){
                    lowerHeight = maxHeightLeft;
                }
                else{
                    lowerHeight = maxHeightRight;
                }
                
                volume = (maxRightIndex - maxLeftIndex) * lowerHeight;
                
                if(volume > maxVolume){
                    maxVolume = volume;
                }
            }
            
            if(maxHeightLeft < maxHeightRight){
                left++;
            }
            else{
                right--;
            }
            
        }
        
        
        
        
        return maxVolume;
        
    }
};