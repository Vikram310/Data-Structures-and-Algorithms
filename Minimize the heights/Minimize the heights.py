def getMinDiff(arr,n,k):
    if(n==1):
        return 0
    #sorting the array
    arr.sort()
    
    #Initialize results
    ans = arr[n-1] - arr[0]
    
    #Handle corner elements
    small = arr[0] +k
    big = arr[n-1] - k
    
    if(small > big):
        small,big = big,small 
    
    #Traverse middle elements
    for i in range(1,n-1):
        sub = arr[i] - k
        add =arr[i] + k
    #if both sub and add doesnt change the diff
        if (sub >= small or add <= big):
            continue
    
    #Either subtraction causes a smaller number or addition causes a greater 
    # number. Update small or big using greedy approach
        if (big - sub <= add -small):
            small = sub
        else:
                big = add
        
        return min(ans, big-small)
    
    
#another 
def getMindiff(self, arr, n, k):
        # code here
        v = []
        taken = [0]*n
        
        for i in range(n):
            if arr[i]-k >= 0:
                v.append([arr[i]-k,i])
            v.append([arr[i] + k,i])
            
        
        v.sort()
        
        elements_in_range = 0;
        left = 0
        right = 0
        
        while elements_in_range < n and right < len(v) :
            
            if taken[v[right][1]] == 0 :
                elements_in_range+=1;
            
            taken[v[right][1]]+=1;
            right+=1;
        
        
        ans = v[right - 1][0] - v[left][0]
        
        while right < len(v) :
    
            if(taken[v[left][1]] == 1) :
                elements_in_range-=1;
            
            taken[v[left][1]]-=1;
            left+=1
            
            while elements_in_range < n and right < len(v) : 
                if taken[v[right][1]] == 0 :
                    elements_in_range+=1
                
                taken[v[right][1]]+=1
                right+=1
            
            
            if(elements_in_range == n) : 
                ans = min(ans, v[right - 1][0] - v[left][0])
            else :
                break
            
        
        return ans
    