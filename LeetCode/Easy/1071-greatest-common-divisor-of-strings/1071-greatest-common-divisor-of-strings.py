from math import gcd 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return str("")
        a = len(str1)
        b = len(str2)
        res = math.gcd(a,b)
        return str1[:res]
