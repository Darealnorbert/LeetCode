class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        allowed_set = set(allowed)
        for word in words:
            if set(word) <= set(allowed):
                count += 1
        return count