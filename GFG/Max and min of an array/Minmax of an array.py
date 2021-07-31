#linear search
class pair:
    def __init__(self):
        self.min=0
        self.max=0

def getMinMax(arr:list, n:int) -> pair:
    minmax=pair()

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax
    
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2,n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax

#Drivercode
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

#tournament method
def getMinMax(low,high,arr):
    arr_max = arr[high]
    arr_min = arr[low]

    if low == high:
        arr_min = arr[low]
        arr_max = arr[high]
        return (arr_max,arr_min)
    
    elif high == low+1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max,arr_min)
    else:
        mid = int((low+high)/2)  
        arr_max1, arr_min1 = getMinMax(low,mid,arr)
        arr_max2, arr_min2 = getMinMax(mid+1,high,arr)
    return (max(arr_max2,arr_max1), min(arr_min1, arr_min2))

#Drivercode
arr = [100,12,567,1,88,1929]
high = len(arr) - 1
low = 0
arr_max,arr_min = getMinMax(low,high,arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max) 

#Compare in Pairs
def getMinMax(arr):
    n = len(arr)
    
    #If array has even number of elements then initialize the first two elements as minimum and maximum
    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
         
        #set the starting index for loop
        i = 2
         
    # If array has odd number of elements then initialize the first element as minimum and maximum
    else:
        mx = mn = arr[0]
         
        # set the starting index for loop
        i = 1
         
    # In the while loop, pick elements in pair and compare the pair with max and min so far
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
             
        # Increment the index by 2 as two elements are processed in loop
        i += 2
     
    return (mx, mn)

if __name__ =='__main__':
     
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)
        
