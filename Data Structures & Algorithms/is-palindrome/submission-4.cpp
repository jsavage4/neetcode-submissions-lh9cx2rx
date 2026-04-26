class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        while(left <= right) {
            if (!isalnum(s[left])) {
                left++;
            } else if (!isalnum(s[right])) {
                right--;
            } else {
                char l = tolower(s[left]);
                char r = tolower(s[right]);
                if (l != r) {
                    return false;
                }
                right--;
                left++;
            }
        }
        return true;
    }
};
