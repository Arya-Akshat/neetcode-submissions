class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total= sum(nums)
        n = len(nums)

        final = n*(n+1)//2
        return final - total