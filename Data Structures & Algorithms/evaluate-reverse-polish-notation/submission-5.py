class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0
        for token in tokens:
            value = token
            if token == '+':
                value = stack.pop() + stack.pop()
            elif token == '-':
                val = stack.pop()
                value = stack.pop() - val
            elif token == '*':
                value = stack.pop() * stack.pop()
            elif token == '/':
                val = stack.pop()
                value = stack.pop() / val
            stack.append(int(value))
        
        return stack.pop()