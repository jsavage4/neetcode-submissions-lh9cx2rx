class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> positioning;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            auto pos_it = positioning.find(complement);
            if (pos_it != positioning.end()) {
                return {pos_it->second, i};
            }
            positioning[nums[i]] = i;
        }
        return {};
    }
};
