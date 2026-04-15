class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        res = []
        for num in nums:
            string = str(num)
            for word in string:
                counter += 1
            res.append(counter)
            counter = 0
        res1 = [x for x in res if x%2 == 0]
        return len(res1)
                
            
        