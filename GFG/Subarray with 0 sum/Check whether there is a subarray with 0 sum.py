#Function to check whether there is a subarray present with 0-sum or not.
def subArrayExists(arr,n):
    ##Your code here
    #using set to store the prefix sum which has appeared already
    s = set()
        
    sum = 0
    #iterating over the array
    for i in range(n):
        #storing prefix sum
        sum += arr[i]
            
        #if prefix sum is 0 or it is already present in set then it is repeated which means 
        #there is subarray whose summation is 0, so we return tru
        if sum == 0 or sum in s:
            return True
                
        #storing every prefix sum obtained in the set
        s.add(sum)
        
    #return false if we dont get any subarray with sum 0
    return False

arr = [4,2,3,3,6]
n = len(arr)
print (subArrayExists(arr, n))