class Solution:
    def isValid(self, s: str) -> bool:
        
        #We can solve this question using Stack and Hashmap, which are like List and dictionary
        stack = []
        ClosetoOpen = { ")":"(", "]":"[", "}":"{" }
        
        #iterating through every character in string
        for c in s:
            
            # checking if the character is a closing parenthesis
            if c in ClosetoOpen:
                
                #checking if stack is not empty and also the latest one in stack is equal to the corresponding opening for closing
                if stack and stack[-1] == ClosetoOpen[c]:
                    stack.pop() #pop the opening from stack, if it matches with the closing 
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        