class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        arr = []
    
        nums.sort()
    
        while nums:
        # Alice removes minimum (first element)
            alice_min = nums.pop(0)
        # Bob removes minimum (now first element)
            bob_min = nums.pop(0)
        
        # According to game rules, Bob appends his removed element first
            arr.append(bob_min)
        # Then Alice appends her removed element
            arr.append(alice_min)
    
        return arr
