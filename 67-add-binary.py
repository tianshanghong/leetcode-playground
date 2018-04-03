# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

# https://leetcode.com/problems/add-binary/description/


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a,2) + int(b,2),'b')