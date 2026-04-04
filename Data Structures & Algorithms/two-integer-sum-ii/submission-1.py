class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):
            left, right = idx + 1, len(numbers) - 1
            complement = target - numbers[idx]
            while left <= right:
                mid = (right + left) // 2
                if numbers[mid] == complement:
                    return [idx + 1, mid + 1]
                if numbers[mid] > complement:
                    right = mid - 1
                else:
                    left = mid + 1
        return None