class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = s.split()
        s_string = "".join(s_list)
        left = 0
        right = len(s_string)-1
        while left<right:
            while left< right and not s_string[left].isalnum():
                left+=1
            while left < right and not s_string[right].isalnum():
                right-=1
            if s_string[left].lower()==s_string[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True
        