class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr = []
        for candy in candies:
            arr.append((candy+extraCandies)>=max(candies))
        return arr
            
        