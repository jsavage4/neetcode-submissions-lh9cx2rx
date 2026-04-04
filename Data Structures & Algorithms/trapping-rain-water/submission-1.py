class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        retVolume = 0
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                retVolume += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                retVolume += maxRight - height[right]
        
        return retVolume