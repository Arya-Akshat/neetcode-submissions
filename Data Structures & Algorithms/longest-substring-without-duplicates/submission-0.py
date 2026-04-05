class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        freq = set()
        for right in range(len(s)):
            
            if s[right] in freq:
                while s[right] in freq:
                    freq.remove(s[left])
                    left+=1
            freq.add(s[right])
            ans = max(ans, right-left+1)


        return ans

        