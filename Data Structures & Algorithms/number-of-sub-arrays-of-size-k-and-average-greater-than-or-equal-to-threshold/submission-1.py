class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        idx = 0
        total = 0
        threshold *= k
        while idx < k:
            total += arr[idx]
            idx += 1
        if total >= threshold:
            count += 1
        while idx < len(arr):
            total -= arr[idx - k]
            total += arr[idx]
            if total >= threshold:
                count += 1
            idx += 1
        return count