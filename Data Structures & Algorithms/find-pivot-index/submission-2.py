class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        trackingB = [0] * (len(nums) + 1)
        n = len(nums)
        for i in range(n):
            trackingB[i+1] = trackingB[i] + nums[i]
        for i in range(n):
            leftSum = trackingB[i]
            rightSum = trackingB[n] - trackingB[i+1]
            if leftSum == rightSum:
                return i
        return -1
        