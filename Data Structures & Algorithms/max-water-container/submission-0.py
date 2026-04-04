class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxVolume = 0
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            maxVolume = max(maxVolume, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxVolume