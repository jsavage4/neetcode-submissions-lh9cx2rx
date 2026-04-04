class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left + 1, right + 1]
            elif currSum > target:
                currVal = numbers[right]
                while numbers[right] == currVal:
                    right -= 1
            else:
                currVal = numbers[left]
                while numbers[left] == currVal:
                    left += 1
        return None