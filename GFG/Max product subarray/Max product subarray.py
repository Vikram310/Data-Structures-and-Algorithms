# Function to find maximum
# product subarray
def maxProduct(arr, n):
	# code here
	#variables to store maxval and minval
	maxval = arr[0]
	minval = arr[0]
		
	maxProd = arr[0]
	for i in range(1,n,1):
	    #if array value is negative we will swap min and maxval
	    if(arr[i]<0):
	        maxval,minval = minval,maxval
		   
	    maxval = max(arr[i],maxval*arr[i])
	    minval = min(arr[i],minval*arr[i])
		
	    maxProd = max(maxProd,maxval)
	   

	return maxProd

arr = [0,0,10,0,0]
n = len(arr)

print(maxProduct(arr, n))