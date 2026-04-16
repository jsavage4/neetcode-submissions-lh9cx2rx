class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = 101;
        int ret = 0;
        for(int& price : prices) {
            if (price < minPrice) {
                minPrice = price;
            }
            int profit = price - minPrice;
            if (profit > ret) {
                ret = profit;
            }
        }
        
        return ret;
    }
};
