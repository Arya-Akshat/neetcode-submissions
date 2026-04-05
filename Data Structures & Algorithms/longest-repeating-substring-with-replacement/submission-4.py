class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        ans = 0
        freq = {}
        for right in range(len(s)):
            right_char = s[right]

            freq[right_char]= freq.get(right_char, 0)+1
            max_freq = max(max_freq, freq[right_char])

            if (right-left+1) - max_freq > k:
                left_char = s[left]
                freq[left_char]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans
