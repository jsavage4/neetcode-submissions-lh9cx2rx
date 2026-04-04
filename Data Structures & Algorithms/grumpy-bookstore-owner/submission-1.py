class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happyCustomers = 0
        lost = maxLost = 0
        for idx in range(len(customers)):
            if grumpy[idx] == 1:
                lost += customers[idx]
            else:
                happyCustomers += customers[idx]

            if idx >= minutes:
                if grumpy[idx - minutes]:
                    lost -= customers[idx - minutes]
            maxLost = max(maxLost, lost)

        return happyCustomers + maxLost
