class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        temp = ""
        i = 0
        while i < len(word1) and i < len(word2):
            temp += word1[i]
            temp += word2[i]
            i += 1
        if len(word1) > len(word2):
            temp += word1[i:]
        else:
            temp += word2[i:]
        return temp