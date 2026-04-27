class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> retTemp (temperatures.size());
        stack<pair<int, int>> temps;
        for (int i = 0; i < temperatures.size(); i++) {
            int temp = temperatures[i];
            while(!temps.empty() and temps.top().first < temp) {
                pair<int, int> t = temps.top();
                retTemp[t.second] = i - t.second;
                temps.pop();
            }
            temps.push({temp, i});
        }
        return retTemp;
    }
};
