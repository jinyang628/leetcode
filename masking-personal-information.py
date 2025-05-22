class Solution:
    def maskEmail(self, s: str) -> str:
        chunks = s.split("@")
        masked_name_lst: list[str] = []
        masked_name_lst.append(s[0].lower())
        masked_name_lst.extend(["*"] * 5)        
        masked_name_lst.append(chunks[0][-1].lower())
        return "".join(masked_name_lst) + "@" + chunks[1].lower()
    def maskPhone(self, s: str) -> str:
        digits: list[str] = [char for char in s if char.isdigit()]
        prefix = ""
        if len(digits) != 10:
            prefix = "+" + (len(digits) - 10) * "*" + "-"
        return prefix + "***" + "-" + "***" + "-" + "".join(digits[-4:])
    def maskPII(self, s: str) -> str:
        if "." in s:
            return self.maskEmail(s)
        return self.maskPhone(s)