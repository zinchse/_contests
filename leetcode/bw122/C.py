class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = nums[0]
        cnt_m = 0
        for num in nums:
            cnt_m += (num == m)
            if num > m and num % m:
                return 1
    
        return (cnt_m + 1) // 2
        