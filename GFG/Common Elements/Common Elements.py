
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i = 0
        j = 0
        k = 0 
        
        last = -12345678
        res = []
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k]:
                if last != A[i]:
                    res.append (A[i])
                    last = A[i]
                i += 1
                j += 1
                k += 1
            
            elif min (A[i], B[j], C[k]) == A[i]:
                i += 1
            elif min (A[i], B[j], C[k]) == B[j]:
                j += 1
            else:
                k += 1
        return res
    
