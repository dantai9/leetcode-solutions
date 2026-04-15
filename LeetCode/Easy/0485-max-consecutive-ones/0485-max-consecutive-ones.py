class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter > res:
                    res = counter
            else:
                counter = 0
                
        return res