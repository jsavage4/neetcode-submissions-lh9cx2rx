class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>> maxHeap;

        for (vector<int>& point : points) {
            int value = (std::pow(point[0], 2)) + std::pow(point[1], 2);
            maxHeap.push({value, point});
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
        vector<vector<int>> retVec;
        while (!maxHeap.empty()) {
            retVec.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return retVec;
    }
};
