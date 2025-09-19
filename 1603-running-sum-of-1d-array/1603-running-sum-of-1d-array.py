class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        sum = 0
        for num in nums:
            sum += num
            arr.append(sum)
        return arr