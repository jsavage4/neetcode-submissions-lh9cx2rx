class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> A;
        for (int i = 0; i < nums.size(); i++) {
            A.push_back({nums[i], i});
        }

        int l = 0;
        int r = nums.size() - 1;
        sort(A.begin(), A.end());

        while (l < r) {
            int currSum = A[l].first + A[r].first;
            if (currSum < target) {
                l++;
            } else if (currSum > target) {
                r--;
            } else {
                return {min(A[l].second, A[r].second),
                        max(A[l].second, A[r].second)};
            }
        }
        return {};
    }
};
