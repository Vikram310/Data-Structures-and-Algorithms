class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        #base case
        if n == 1:
            return "1"
        
        #recursion 
        previous = self.countAndSay(n-1)
        res = "" #intialise empty string to strore result
        count = 1 #initialise count with 1 
        
        for i in range(len(previous)):
            if i == len(previous) -1 or previous[i] != previous[i+1]:
                res += str(count) + previous[i]
                count = 1
            else:
                count += 1
        return res 