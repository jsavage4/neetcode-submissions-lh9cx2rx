class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set({'+', '-', '*', '/'})
        stack = []
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                if token == '+':
                    currVal = stack.pop() + stack.pop()
                    stack.append(currVal)
                elif token == '-':
                    firstVal = stack.pop()
                    currVal = stack.pop() - firstVal
                    stack.append(currVal)
                elif token == '*':
                    currVal = stack.pop() * stack.pop()
                    stack.append(currVal)
                elif token == '/':
                    firstVal = stack.pop()
                    currVal = int(stack.pop() / firstVal)
                    stack.append(currVal)
        return stack.pop()
