class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retArr = []
        right, left = 0, 0
        currWindow = []
        while right < k - 1:
            heapq.heappush(currWindow, (-nums[right], right))
            right += 1
        while right < len(nums):
            # if nums[left] != maxNum:
            #     ret.append(maxNum)
            # else:
            #     # Get second most Common somehow
            heapq.heappush(currWindow, (-nums[right], right))
            while currWindow[0][1] < left:
                heapq.heappop(currWindow)
            retArr.append(-currWindow[0][0])
            left += 1
            right += 1
        return retArr