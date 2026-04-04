class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        prev = None
        for num in nums:
            if prev == num:
                return True
            prev = num
        return False