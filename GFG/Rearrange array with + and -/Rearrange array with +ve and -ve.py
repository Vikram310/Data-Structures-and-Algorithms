def rearrange(arr,n):
        #sort the array first
        arr.sort()
        
        #initialize two pointers each for positive i and negative j
        i,j = 1,1
        while i<n:
            if (arr[i] > 0):
                break
            i += 1
            
        #swap numbers until given condition is met
        while(arr[j] < 0) and (j<n):
            arr[i],arr[j] = arr[j],arr[i]
            #increment negative pointer by 2 as they are alternative
            j += 2
            i += 1
            
        return arr

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
 
ans = rearrange(arr, len(arr))
for num in ans:
    print(num, end = " ")