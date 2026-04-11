class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = set()
        for i in nums:
            if i in arr:
                return i 
            else:
                arr.add(i)