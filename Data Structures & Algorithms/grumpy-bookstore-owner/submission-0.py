class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        lostCustomers = [0] * len(customers)
        happyCustomers = 0
        for idx in range(len(customers)):
            if grumpy[idx] == 1:
                lostCustomers[idx] = customers[idx]
            else:
                happyCustomers += customers[idx]
        
        lost = maxLost = 0
        n = len(lostCustomers)
        for idx in range(n):
            if idx < minutes:
                lost += lostCustomers[idx]
            else:
                lost += lostCustomers[idx] - lostCustomers[idx - minutes]
            maxLost = max(lost, maxLost)
        return happyCustomers + maxLost

# lost = lost - x
# lost = lost + y

# lost = lost + 
