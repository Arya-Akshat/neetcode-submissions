class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroes = 0
        for i in nums:
            if i!= 0:
                total*=i
            else:
                zeroes+=1
        if zeroes>1:
            return [0]*(len(nums))
        ans = []
        for j in nums:
            if j!=0 and zeroes == 0:
                ans.append(total//j)
            elif j!=0 and zeroes == 1:
                ans.append(0)
            else:
                ans.append(total)
        return ans

        
        