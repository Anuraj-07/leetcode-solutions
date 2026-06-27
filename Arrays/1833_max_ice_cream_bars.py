## 1833. Maximum Ice Cream Bars

Difficulty: Medium

Approach:
- Sort the costs.
- Buy the cheapest ice creams first.
- Stop when coins are insufficient.

Time Complexity:
O(n log n)

Space Complexity:
O(1)

Status: Solved Myself!

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        l=0
        costs.sort()
        for i in costs:
            if coins>=i:
                l+=1
                coins-=i
        return (l)
        
