def inversionCount(arr, n):
        temp_arr = [0]*n #temp_arr is created to store the sorted array in merge function
        return mergesort(arr,temp_arr,0,n-1)
    
def mergesort(arr,temp_arr,left,right):
    inv_count = 0 #used to calculate the number of inversions in each recursive call 
    if left < right:
        mid = (left+right)//2 #mid is calculated to divide the array into two pieces
        inv_count += mergesort(arr,temp_arr,left,mid) #for left sub-array
        inv_count += mergesort(arr,temp_arr,mid+1,right) #for right sub-array
        inv_count += merge(arr,temp_arr,left,mid,right) #for merging the left and right sub-arrays
    return inv_count

def merge(arr,temp_arr,left,mid,right):
    i = left #starting index of left subarray
    j = mid+1 #starting index of right sub-array
    k = left #starting index of the final sorted array
    inv_count = 0
        
    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i] #as there will be no inversions if arr[i] <= arr[j]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j] #inversion will occur
            inv_count += (mid+1 - i) #as all the elements to the right of i will also be greater
            k += 1
            j += 1
        
    while i <= mid:
        temp_arr[k] = arr[i]#copying remaining elemnts of left subarray
        k += 1
        i += 1
        
    while j <= right:
        temp_arr[k] = arr[j] #copying remaining elements of right subarray
        k += 1
        j += 1
            
        #copy sorted array to original array
    for loop_var in range(left,right+1):
        arr[loop_var] = temp_arr[loop_var]
            
    return inv_count
