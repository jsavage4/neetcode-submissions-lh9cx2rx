class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        trackingB = [0] * len(nums)
        for idx, num in enumerate(nums):
            if idx > 0:
                trackingB[idx] += trackingB[idx-1] + nums[idx-1]
        trackingA = [0] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            if idx < len(nums) - 1:
                trackingA[idx] += trackingA[idx + 1] + nums[idx + 1]
        for idx in range(len(nums)):
            if trackingA[idx] == trackingB[idx]:
                return idx
        return -1
        