class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                c += 1
        return c
                
            
        