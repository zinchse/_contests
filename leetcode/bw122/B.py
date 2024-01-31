class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def get_num_bits(el):
            return sum([c == "1" for c in bin(el)])        
        
        for slow in range(len(nums)):
            for fast in range(slow + 1, len(nums)):
                if nums[slow] > nums[fast] and get_num_bits(nums[slow]) != get_num_bits(nums[fast]):
                    return False
        
        return True
        