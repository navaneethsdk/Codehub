class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i,j = 0, n=nums.size();
        for(i=1; i<n; i++){
            if(nums[i] != nums[j]){
                j++;
                nums[j] = nums[i];
            }
        }   
        return i+1;
    }
 
};
