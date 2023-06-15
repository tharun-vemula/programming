"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        return candidate
