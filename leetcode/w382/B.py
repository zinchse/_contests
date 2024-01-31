from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cnt = Counter(nums)
        
        @lru_cache(None)
        def helper(num: int) -> int:
            if cnt[num * num] and cnt[num] >= 2:
                return 2 + helper(num * num)
            else:
                return 1
            
        res = 0
        for num in nums:
            if num == 1:
                res = max(res, cnt[num] - (cnt[num] % 2 == 0))
            else:
                res = max(res, helper(num))

        return res
        
