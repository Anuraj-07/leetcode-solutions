
Problem: Count Majority Subarrays

Topic: Arrays, Brute Force

Difficulty: Medium

Approach:
1. Consider every possible subarray.
2. Keep track of how many times the target appears.
3. For each subarray, check whether:
      target_count > length / 2
4. If true, increment the answer.

Time Complexity: O(n²)

Space Complexity: O(1)

Status: Editorial Assisted


class Solution:
    def countMajoritySubarrays(self, nums, target):

        n = len(nums)
        total_subarrays = 0

        # Iterate over all starting positions
        for i in range(n):

            target_count = 0

            # Expand subarray to the right
            for j in range(i, n):

                if nums[j] == target:
                    target_count += 1

                length = j - i + 1

                if target_count * 2 > length:
                    total_subarrays += 1

        return total_subarrays
