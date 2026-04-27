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
        for (auto& [key, value] : s_freq) {
            if (t_freq[key] != value) return false;
        }
        return true;
    }
};
