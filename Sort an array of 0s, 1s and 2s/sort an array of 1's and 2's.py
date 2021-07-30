class Solution:
    def sort012(self, arr, n):
        low = 0
        high = n-1
        mid = 0
        while mid <= high:
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]
                high-=1


#Another approach
#Utility function to print the contents of array

def printarr(arr, n):
    for i in range(n):
        print(arr[i],end =" ")

def sortarr(arr,n):
    cnt0=0
    cnt1=0
    cnt2=0

    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i]==1:
            cnt1 += 1
        else:
            cnt2 += 1
        i=0
    while (cnt0>0):
        arr[i] = 0
        i+=1
        cnt0-=1
    while(cnt1>0):
        arr[i] = 1
        i+=1
        cnt1-=1
    while(cnt2>0):
        arr[i] = 2
        i+=1
        cnt2 -= 1
    
    printarr(arr,n)

#Driver code
arr = [1,1,2,0,1,0,0,0,2,1]
n=len(arr)

sortarr(arr,n)

    
