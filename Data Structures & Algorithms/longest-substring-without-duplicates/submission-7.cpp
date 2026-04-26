class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t left = 0;
        int retLength = 0;
        std::set<char> mySet;
        for (size_t i = 0; i < s.size(); ++i) {
            char c = s[i];
            auto mySet_it = mySet.find(c);
            if (mySet_it != mySet.end()) {
                while (s[left] != c) {
                    mySet.erase(s[left]);
                    ++left;
                }
                mySet.erase(s[left]);
                ++left;
            }
            mySet.insert(c);
            if (mySet.size() > retLength) {
                retLength = mySet.size();
            }
        }
        return retLength;
    }
};
