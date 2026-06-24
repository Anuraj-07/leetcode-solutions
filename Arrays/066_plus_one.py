#Status: Editorial Assisted

LeetCode: #66

Problem: Plus One


Topic: Arrays, Math

Difficulty: Easy

Approach:
1. Convert the digits array into a number.
2. Add 1 to the number.
3. Convert the updated number back into an array.

Time Complexity: O(n)

Space Complexity: O(n)

Note:
This is a straightforward beginner-friendly approach.
An optimized in-place solution exists that avoids converting the entire array into a number.

class Solution:
    def plusOne(self, digits):

        num = 0
        L = []

        for i in digits:
            num = num * 10 + i

        num = num + 1

        while num > 0:

            a = num % 10

            num = num // 10

            L.insert(0, a)

        return L
