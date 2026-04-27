class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> retVec;
        retVec.reserve(strs.size());
        vector<pair<unordered_map<char, int>, int>> existingFreqs;
        int nextIdx = 0;

        for (string& str : strs) {
            unordered_map<char, int> strFreq;
            for (char c : str) {
                strFreq[c]++;
            }
            int insertIdx = nextIdx;
            for (auto& freqPairs : existingFreqs) {
                bool foundMatch = true;
                if (freqPairs.first.size() != strFreq.size()) {
                    foundMatch = false;
                }
                for (auto& kv : freqPairs.first) {
                    if (strFreq[kv.first] != kv.second) {
                        foundMatch = false;
                    }
                }
                if (foundMatch) {
                    insertIdx = freqPairs.second;
                    break;
                }
            }
            if (insertIdx == nextIdx) {
                existingFreqs.push_back({strFreq, insertIdx});
                retVec.push_back({str});
                nextIdx++;
            } else {
                retVec[insertIdx].push_back(str);
            }
        }
        return retVec;
    }
};
