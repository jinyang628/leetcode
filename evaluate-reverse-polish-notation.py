class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            match token:
                case "+":    
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
                case _:
                    stack.append(int(token))
        return stack[0]