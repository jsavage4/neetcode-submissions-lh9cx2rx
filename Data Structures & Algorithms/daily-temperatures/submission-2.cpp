class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> retTemp (temperatures.size());
        std::stack<std::pair<int, int>> myStack;
        for (int i = 0; i < temperatures.size(); i++) {
            while (!myStack.empty() and myStack.top().second < temperatures[i]) {
                std::pair<int, int> poppedPair = myStack.top();
                myStack.pop();
                retTemp[poppedPair.first] = i - poppedPair.first;
            }
            myStack.push({i, temperatures[i]});
        }
        return retTemp;
    }
};
