class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        track = set()
        for email in emails:
            splitted = email.split("@")
            left, right = splitted[0], splitted[1]
            left_lst = []
            for char in left:
                if char == ".":
                    continue
                if char == "+":
                    break      
                left_lst.append(char)
            left = "".join(left_lst)
            email = left + "@" + right
            track.add(email)
        return len(track)