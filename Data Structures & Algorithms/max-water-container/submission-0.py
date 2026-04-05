class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        curr_cap = 0
        left = 0
        right = len(heights)-1
        while left< right:
            height = min(heights[left], heights[right])
            width = right-left 
            curr_cap = height*width
            ans = max(curr_cap, ans)
            if heights[left]< heights[right]:
                left+=1
            else:
                right-=1
        return ans
                

        