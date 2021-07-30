class Solution:
    def swap(self,arr, a, b): 
        temp = arr[a] 
        arr[a] = arr[b] 
        arr[b] = temp 
      
    def randomPartition(self,arr, l, r): 
        n = r - l + 1
        pivot = int(random.random() % n)  
        self.swap(arr, l + pivot, r)  
        return self.partition(arr, l, r) 
    def kthSmallest(self,arr, l, r, k): 
        if (k > 0 and k <= r - l + 1): 
              
            pos = self.randomPartition(arr, l, r)  
            if (pos - l == k - 1):  
                return arr[pos]  
            if (pos - l > k - 1):  
                                 
                return self.kthSmallest(arr, l, pos - 1, k)  
      
            
            return self.kthSmallest(arr, pos + 1, r,  
                               k - pos + l - 1) 
      
        return 999999999999
      
    def partition(self,arr, l, r): 
        x = arr[r] 
        i = l 
        for j in range(l, r): 
            if (arr[j] <= x): 
                self.swap(arr, i, j)  
                i += 1
        self.swap(arr, i, r)  
        return i

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L,M = len(left),len(mid)

        if k <= L:  
            return self.findKthLargest(left,k)
        elif k > (L+M):
            return self.findKthLargest(right,k-(L+M))
        else:
            return mid[0]