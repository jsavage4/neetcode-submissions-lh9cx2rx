class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positioning = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in positioning:
                return [positioning[complement], idx]
            positioning[num] = idx
        return None
