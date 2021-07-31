def minJumps(arr, n):
    if (n<=1):   # The number of jumps needed to reach the starting index is 0
        return 0
   
    if (arr[0] == 0): # Return -1 if not possible to jump
        return -1
	   
    maxreach = arr[0] #stores all time the maximal reachable index in the array
    step = arr[0] #stores the amount of steps it will still take
    jump = 1 #stores the amount of jumps necessary to reach that maximal reachable position
	    
    for i in range(1,n):#start traversing the array
        if (i == n-1):# Check if we have reached the end of the array
            return jump
	        
        maxreach = max(maxreach, i+arr[i]) #updating maxReach
        step -= 1#USe a step to get the current index
	         
        if(step == 0):#if no further steps left
            jump += 1 #we used a jump
	            
            if(i>=maxreach):## Check if the current index / position or lesser index is the maximum reach point from the previous indexes
                return -1
	                
            step = maxreach - i ## re-initialize the steps to the amount of steps to reach maxReach from position i
    return -1

#Drivercode
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

print(minJumps(arr,n))