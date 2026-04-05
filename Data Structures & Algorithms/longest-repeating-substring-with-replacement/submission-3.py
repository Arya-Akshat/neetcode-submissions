class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Pointers for the window and frequency map for characters in the window
        left = 0
        max_length = 0
        max_freq = 0
        freq = {}
        
        # 'right' pointer expands the window
        for right in range(len(s)):
            right_char = s[right]
            
            # Update the frequency of the new character in the window
            freq[right_char] = freq.get(right_char, 0) + 1
            
            # Update the frequency of the most common character so far
            max_freq = max(max_freq, freq[right_char])
            
            # The current window size is (right - left + 1).
            # The number of characters to replace is (window_size - max_freq).
            # If this number is greater than k, the window is invalid, so we shrink it.
            if (right - left + 1) - max_freq > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
            
            # The current window is the longest we've seen so far
            # because we only expand it.
            max_length = max(max_length, right - left + 1)
            
        return max_length