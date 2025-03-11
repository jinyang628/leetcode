class Solution:
    def numDecodings(self, s: str) -> int:
        track = {}
        def helper(text: str):
            if not text:
                return 1
            if text[0] == "0":
                return 0
            if len(text) == 1:
                return 1
            if text in track:
                return track[text]
            # larger than 2 characters
            one = helper(text[1:])
            if int(text[:2]) <= 26:
                track[text] = one + helper(text[2:])
            else:
                track[text] = one
            return track[text]
        return helper(s)