from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            mp[key].append(word)
        
        return list(mp.values())