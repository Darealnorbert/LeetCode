class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = 0
        sum2 = 0
        for num in nums:
            if num < 10:
                sum1 += num
            else:
                sum2 += num
        if sum1 == sum2:
            return False
        else:
            return True
