class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int retLength = 0;
        std::unordered_set<char> mySet;
        for (int right = 0; right < s.size(); ++right) {
            // char c = s[i];
            // auto mySet_it = mySet.find(c);
            // if (mySet_it != mySet.end()) {
            //     while (s[left] != c) {
            //         mySet.erase(s[left]);
            //         ++left;
            //     }
            //     mySet.erase(s[left]);
            //     ++left;
            // }
            // mySet.insert(c);
            // if (mySet.size() > retLength) {
            //     retLength = mySet.size();
            // }
            while(mySet.find(s[right]) != mySet.end()) {
                mySet.erase(s[left]);
                left++;
            }
            mySet.insert(s[right]);
            retLength = max(retLength, right - left + 1);

        }
        return retLength;
    }
};
