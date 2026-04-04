class Solution:
    def findMin(self, nums: List[int]) -> int:
        ret = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                ret = min(ret, nums[left])
                break
            mid = (left + right) // 2
            ret = min(ret, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return ret