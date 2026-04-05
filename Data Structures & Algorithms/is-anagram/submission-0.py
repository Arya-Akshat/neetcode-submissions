from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freq1[s[i]]+=1
            freq2[t[i]]+=1
        for key in freq1.keys():
            if freq1[key] != freq2[key]:
                return False
        return True
        