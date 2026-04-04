class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        trackingB = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            trackingB[i+1] = trackingB[i] + nums[i]
        for i in range(len(nums)):
            leftSum = trackingB[i]
            rightSum = trackingB[len(nums)] - trackingB[i+1]
            if leftSum == rightSum:
                return i
        return -1
        