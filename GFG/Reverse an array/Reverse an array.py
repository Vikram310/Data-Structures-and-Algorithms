#Iterative way
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 

#Recursive way
def reverselist(B, start, end):
    if start >= end:
        return
        B[start],B[end] = B[end],B[start]
        reverselist(B,start+1,end-1)



#List Slicing way
def reverseList(A):
    print(A[::-1])
