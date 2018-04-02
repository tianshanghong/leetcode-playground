# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)):
            if not digits[-(i+1)] == 9:
                digits[-(i+1)] = digits[-(i+1)] + 1
                return digits
            else:
                digits[-(i+1)] = 0
                
        digits.insert(0, 1)
        return digits
