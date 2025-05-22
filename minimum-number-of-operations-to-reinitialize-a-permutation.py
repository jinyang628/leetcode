class Solution:
    def reinitializePermutation(self, n: int) -> int:
        target = [i for i in range(n)]
        transformed = target
        def is_equal(a: list[int], b:list[int]) -> bool:
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            return True
        def transform(arr: list[int]) -> list[int]:
            res = []
            for i in range(len(arr)):
                if i % 2 == 0:
                    res.append(arr[i // 2])
                else:
                    res.append(arr[len(arr) // 2 + (i - 1) // 2])
            return res
        count = 0
        while True:
            transformed = transform(transformed)
            if is_equal(transformed, target):
                return count + 1
            count += 1