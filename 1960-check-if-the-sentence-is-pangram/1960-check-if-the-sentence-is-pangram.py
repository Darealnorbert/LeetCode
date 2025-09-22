import string
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        arr = set(string.ascii_lowercase)
        str = set(sentence)
        return str >= arr
        