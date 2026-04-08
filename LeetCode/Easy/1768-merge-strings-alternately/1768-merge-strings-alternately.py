class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        final_list = []
        lenght = len(list1) + len(list2)
        for i in range(lenght):
            if i < len(list1):  
                final_list.append(list1[i])
            if i < len(list2):
             final_list.append(list2[i])
        return ''.join(final_list)