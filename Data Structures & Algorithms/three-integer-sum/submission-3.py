class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue
            l, r = idx + 1, len(nums) - 1
            target = -num
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    oldL = nums[l]
                    oldR = nums[r]
                    while l < len(nums) and nums[l] == oldL:
                        l += 1
                    while r > 0 and nums[r] == oldR:
                        r -= 1
        return ret