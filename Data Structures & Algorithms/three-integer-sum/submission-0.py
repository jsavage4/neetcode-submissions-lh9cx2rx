class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ret = []
        for idx, anchor in enumerate(nums):
            if anchor in seen:
                continue
            seen.add(anchor)
            if anchor > 0:
                break
            left, right = idx + 1, len(nums) - 1
            target = -anchor

            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == target:
                    ret.append([anchor, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                if currSum > target:
                    right -= 1
                else:
                    left += 1
        return ret