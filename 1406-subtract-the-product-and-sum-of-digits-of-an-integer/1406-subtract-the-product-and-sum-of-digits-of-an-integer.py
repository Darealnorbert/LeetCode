class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        string = str(n)
        list = [int(var) for var in string]
        for val in list:
            sum += val
            product *= val
        return product - sum

        

        
            