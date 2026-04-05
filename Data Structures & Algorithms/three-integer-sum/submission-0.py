class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if (i-1>=0 and nums[i]== nums[i-1]) :
                continue
            if nums[i]>0:
                break
            left = i+1
            right = len(nums)-1
            while left < right:
                

                val = nums[i]+ nums[left]+ nums[right]
                if val == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    if left - 1>i and nums[left] == nums[left-1]:
                        left+=1
                    if right+1 < len(nums) and nums[right] == nums[right+1]:
                        right-=1 

                elif val > 0:
                    right-=1
                else:
                    left+=1
        return ans
            

        