class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(1,len(s)):
            if (s[i-1].lower() != s[i].lower()):
                count+=1
        return count

        