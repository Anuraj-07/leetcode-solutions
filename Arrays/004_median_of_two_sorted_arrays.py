Problem: Median of Two Sorted Arrays

LeetCode: #4

Topic: Arrays, Sorting

Difficulty: Hard

Approach:
1. Merge both arrays.
2. Sort the merged array.
3. If the length is odd, return the middle element.
4. If the length is even, return the average of the two middle elements.

Time Complexity: O((m+n) log(m+n))

Space Complexity: O(m+n)

Note:
This is a beginner-friendly brute-force approach.
An optimized O(log(min(m,n))) binary search solution exists.

Solution:-

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        result = nums1 + nums2
        l = sorted(result)
        if len(l) % 2 != 0:
            e = len(l) // 2
            return l[e]

        else:
            m = len(l) // 2
            r = (l[m] + l[m-1]) / 2
            return r
