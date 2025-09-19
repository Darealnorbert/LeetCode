class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        nums = [int(val) for val in str(num)]
        for i in nums:
            if num % i == 0:
                count += 1
        return count