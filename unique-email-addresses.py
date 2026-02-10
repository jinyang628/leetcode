1from collections import Counter
2class Solution:
3    def numUniqueEmails(self, emails: List[str]) -> int:
4        counter = Counter()
5        for email in emails:
6            local_name, domain = email.split("@")
7            local_name = local_name.replace(".", "")
8            local_name = local_name.split("+")[0]
9            print(local_name, domain)
10            counter[f"{local_name}@{domain}"] += 1
11        return len(counter)