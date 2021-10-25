# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


#include <vector>
#include <algorithm>


class Solution {
public:
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        int arrSize = nums.size();
        
        int i,j,k;
        vector<vector<int>> answer;
        
        int numsSize = sizeof(nums) / sizeof(nums[0]);
        
        sort(nums.begin(), nums.end());
        

    
        vector<vector<int> > res;

        for (int i = 0; i < nums.size(); i++) {

            int target = -nums[i];
            int front = i + 1;
            int back = nums.size() - 1;

            while (front < back) {

                int sum = nums[front] + nums[back];

                // Finding answer which start from number num[i]
                if (sum < target)
                    front++;

                else if (sum > target)
                    back--;

                else {
                    vector<int> triplet = {nums[i], nums[front], nums[back]};
                    res.push_back(triplet);

                    // Processing duplicates of Number 2
                    // Rolling the front pointer to the next different number forwards
                    while (front < back && nums[front] == triplet[1]) front++;

                    // Processing duplicates of Number 3
                    // Rolling the back pointer to the next different number backwards
                    while (front < back && nums[back] == triplet[2]) back--;
                }

            }

            // Processing duplicates of Number 1
            while (i + 1 < nums.size() && nums[i + 1] == nums[i]) 
                i++;

        }

        return res;
    

        
//         int currentNum = 1000000;
//         int currentNum2 = 1000000;
            
//         for(i = 0; i < arrSize - 2; i++){
//             if(currentNum != nums[i]){
//                 currentNum = nums[i];
//                 for(j = i + 1; j < arrSize - 1; j++){
//                     cout << "Here2";
                    
//                     if(currentNum2 != nums[j]){
//                         currentNum2 = nums[j];
//                         for(k = j + 1; k < arrSize; k++){
//                             cout << "Here";
//                             if(nums[i] + nums[j] + nums[k] == 0){

//                                 cout << "Here3";
//                                 int triplet[] = {nums[i], nums[j], nums[k]};
//                                 int tripletSize = sizeof(triplet) / sizeof(triplet[0]);

//                                 sort(triplet, triplet + tripletSize);

//                                 vector<int> tripletVector (triplet, triplet + sizeof(triplet) / sizeof(int));

//                                 if(find(answer.begin(), answer.end(), tripletVector) == answer.end()){
//                                     answer.push_back(tripletVector);
//                                 }
//                             }
//                         }
//                     }
//                 }
//             }            
//         }
        
        //return answer;
        
    }
};