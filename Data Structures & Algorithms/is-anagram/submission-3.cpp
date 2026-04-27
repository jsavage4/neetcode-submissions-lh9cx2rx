class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_freq;
        std::unordered_map<char, int> t_freq;

        if (s.size() != t.size()) return false;

        for (size_t i = 0; i < s.size(); i++) {
            s_freq[s[i]]++;
            t_freq[t[i]]++;
        }
        for (auto& kv : s_freq) {
            if (t_freq[kv.first] != kv.second) return false;
        }
        return true;
    }
};
