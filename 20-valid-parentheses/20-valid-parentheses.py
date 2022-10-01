class Solution:
    def isValid(self, s: str) -> bool:
        
        #We can solve this question using Stack and Hashmap, which are like List and dictionary
        stack = []
        ClosetoOpen = { ")":"(", "]":"[", "}":"{" }
        
        for c in s:
            if c in ClosetoOpen:
                if stack and stack[-1] == ClosetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        