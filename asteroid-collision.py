class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
                continue 
            exit = False
            while not exit:
                if not stack:
                    stack.append(num)
                    exit = True
                elif stack[-1] < 0:
                    stack.append(num)
                    exit = True
                elif stack[-1] == abs(num):
                    stack.pop()
                    exit = True
                elif stack[-1] < abs(num):
                    stack.pop()
                else:
                    exit = True
        return stack