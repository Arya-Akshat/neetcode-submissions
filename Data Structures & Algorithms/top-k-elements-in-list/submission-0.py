class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums_ = Counter(nums)
        ans = []
        index = 0
        for key, val in nums_.most_common(k):
            ans.append(key)

        return ans