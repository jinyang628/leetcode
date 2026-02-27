1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        ransomNote = Counter(ransomNote)
4        magazine = Counter(magazine)
5        for key, freq in ransomNote.items():
6            if magazine[key] < freq:
7                return False
8        return True