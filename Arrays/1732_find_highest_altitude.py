# 1732. Find the Highest Altitude

## Approach
- The biker starts at altitude `0`.
- Maintain the current altitude by adding each value from `gain`.
- Keep updating the maximum altitude reached during the journey.

## Algorithm
1. Initialize `current = 0` and `highest = 0`.
2. Traverse the `gain` array.
3. Update the current altitude.
4. Update the highest altitude if needed.
5. Return the highest altitude.

## Complexity
- Time: O(n)
- Space: O(1)
Status: Solved Myself!!
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max=0
        sum=0
        if len(gain)>0:
            for i in gain:
                sum+=i
                if sum>max:
                    max=sum
        return max
