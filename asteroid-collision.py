class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)
            else:
                while stack:
                    curr = stack[-1]
                    if curr < 0:
                        stack.append(asteroid)
                        break
                    elif stack[-1] > abs(asteroid):
                        break
                    else:
                        stack.pop()
                        if curr == abs(asteroid):
                            break
                        if not stack:
                            stack.append(asteroid)
                            break
        return stack