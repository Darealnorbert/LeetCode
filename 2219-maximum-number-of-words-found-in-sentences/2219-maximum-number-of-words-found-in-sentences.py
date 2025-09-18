class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        hashmap = {}
        arr = []
        for sentence in sentences:
            for number,val in enumerate(sentence.split()):
                number +=1
            hashmap[sentence] = number
            arr.append(number)
        return max(arr)
