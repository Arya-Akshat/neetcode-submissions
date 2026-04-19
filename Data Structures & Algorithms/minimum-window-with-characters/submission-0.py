from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        window = defaultdict(int)
        required = len(need)
        formed = 0
        left = 0
        ans = ""

        for right in range(len(s)):
            char = s[right]
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    formed += 1
            while formed == required:
                if ans == "" or (right - left + 1) < len(ans):
                    ans = s[left:right+1]

                left_char = s[left]
                if left_char in need:
                    window[left_char] -= 1
                    if window[left_char] < need[left_char]:
                        formed -= 1
                left += 1

        return ans