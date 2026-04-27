class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int front = 0, back = matrix.size() - 1;
        int arrIdx = -1; 
        while (front <= back) {
            int mid = (front + back) / 2;
            if (matrix[mid][0] > target) {
                back = mid - 1;
            } else if (matrix[mid][matrix[mid].size() - 1] < target) {
                front = mid + 1;
            } else {
                arrIdx = mid;
                break;
            }
        }
        if (arrIdx == -1) return false;
        int l = 0, r = matrix[arrIdx].size() - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (matrix[arrIdx][mid] > target) {
                r = mid - 1;
            } else if (matrix[arrIdx][mid] < target) {
                l = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
