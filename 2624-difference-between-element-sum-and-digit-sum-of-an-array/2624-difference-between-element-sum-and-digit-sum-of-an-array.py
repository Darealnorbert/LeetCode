class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        dig_sum = 0
        for num in nums:
            sum += num
            for val in str(num):
                dig_sum += int(val)
        return abs(dig_sum - sum)

            
        return abs()

        