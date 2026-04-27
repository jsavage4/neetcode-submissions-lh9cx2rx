class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        unordered_map<int,int> freq;
        for (auto& num : nums) {
            freq[num]++;
        }
        for (auto& kv : freq) {
            minHeap.push({kv.second, kv.first});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        vector<int> retVec;
        while (!minHeap.empty()) {
            retVec.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return retVec;
    }
};
