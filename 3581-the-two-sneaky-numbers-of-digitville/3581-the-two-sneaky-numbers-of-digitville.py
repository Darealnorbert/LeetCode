class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        arr = []
        for i, num in enumerate(nums):
            if num in hashmap:
                arr.append(num)
            hashmap[num] = i
        return arr
            

        