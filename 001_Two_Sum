Question : Two Sum 
Topics : Arrays, Hash Map
Difficulty: Easy
Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(int(nums[i])+int(nums[j])==target):
                    return [i,j]
                    flag=1
        if flag ==0:
            return None
