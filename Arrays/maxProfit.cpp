class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i=0, valley = prices[0], peak = prices[0], maxProfit = 0;
        int n = prices.size();
        while(i < n-1){
            while(i < n-1 && prices[i] >= prices[i+1])
                i++;
                valley = prices[i];                
            
            
            while(i < n-1 && prices[i] <= prices[i+1])
                i++;
                peak = prices[i];
                maxProfit += peak - valley;
        }
        return maxProfit;    
    }
};
