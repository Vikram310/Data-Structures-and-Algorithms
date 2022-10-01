class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        if len(strs) == 0:
            return res
        
        #we need to just iterate until the length of smallest string in list, so lets find the length
        minlen= len(strs[0])
        for i in range(len(strs)):
            minlen = min(minlen, len(strs[i]))
        
        i = 0  
        while i < minlen:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return res
            res = res+char
            i+=1
        return res