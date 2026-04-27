class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string& str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            groups[key].push_back(str);
        }
        vector<vector<string>> retVec;
        for (auto& kv : groups) {
            retVec.push_back(kv.second);
        }
        return retVec;
    }
};
