class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in values:
                return [values[complement], idx]
            values[num] = idx
        return None