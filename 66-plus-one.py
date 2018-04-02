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
