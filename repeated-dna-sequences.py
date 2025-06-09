class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        st=set()
        d={}
        for i in range(len(s)-9):
            if s[i:i+10] in d:
                st.add(s[i:i+10])
            else:
                d[s[i:i+10]]=1
        return list(st)