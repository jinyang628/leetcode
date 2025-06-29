class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        curr = ""
        stack = []
        while i < len(s):
            if s[i] == " ":
                pass
            elif s[i].isdigit():
                curr += s[i]
            else:
                stack.append(int(curr))
                curr = ""
                stack.append(s[i])
            i += 1
        stack.append(int(curr))
        new_stack = []
        i = 0
        while i < len(stack):
            if stack[i] == "*":
                new_stack.append(
                    new_stack.pop() * stack[i + 1]
                )
                i += 2
            elif stack[i] == "/":
                new_stack.append(
                    math.floor(new_stack.pop() / stack[i + 1])
                )
                i += 2
            else:
                new_stack.append(stack[i])
                i += 1
        base = new_stack[0]
        for i in range(1, len(new_stack), 2):
            operator, digit = new_stack[i], new_stack[i + 1]
            if operator == "+":
                base += digit
            else:
                base -= digit
        return base