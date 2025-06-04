class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for operation in operations:
            print(res)
            if operation.isdigit() or operation[0] == "-":
                res.append(int(operation))
            elif operation == "+":
                res.append(res[-2] + res[-1])
            elif operation == "C":
                res.pop()
            elif operation == "D":
                res.append(res[-1] * 2)
        return sum(res)