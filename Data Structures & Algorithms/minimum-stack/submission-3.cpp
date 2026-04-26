class MinStack {
private:
    std::stack<int> myStack;
    std::stack<int> minStack;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        myStack.push(val);
        val = min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        myStack.pop();
        minStack.pop();
    }
    
    int top() {
        return myStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
