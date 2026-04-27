class KthLargest {
private:
    int threshold_;
    priority_queue<int, vector<int>, greater<int>> minHeap_;
public:
    KthLargest(int k, vector<int>& nums) {
        threshold_ = k;
        for (auto& num : nums) {
            minHeap_.push(num);
            if (minHeap_.size() > threshold_) {
                minHeap_.pop();
            }
        }
    }
    
    int add(int val) {
        minHeap_.push(val);
        if (minHeap_.size() > threshold_) {
            minHeap_.pop();
        }
        return minHeap_.top();
    }
};
