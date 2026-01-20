1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        str_lst = list(s)
45        vowel_idx_and_char = [] # (idx, char)
6        vowels = {"a", "e", "i", "o", "u"}
78        for idx, char in enumerate(s):
9            if char.lower() in vowels:
10                vowel_idx_and_char.append((idx, char))
1112        left, right = 0, len(vowel_idx_and_char) - 1
13        while left < right:
14            left_idx, left_char = vowel_idx_and_char[left]
15            right_idx, right_char = vowel_idx_and_char[right]
16            str_lst[left_idx], str_lst[right_idx] = right_char, left_char
17            left += 1
18            right -= 1
1920        return "".join(str_lst)