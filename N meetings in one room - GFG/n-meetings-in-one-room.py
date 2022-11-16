#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        # for first zip
        start_end = []
        for i,j in zip(start,end):
            start_end.append([i,j])
        
        #second zip
        res = []
        for i,j in enumerate(start_end):
            res.append([i,j[0],j[1]])
        
        #sort
        res.sort(key = lambda pair: pair[2])
        
        #calculate
        last_time = 0 
        count = 0
        for i in range(n):
            if res[i][1] > last_time:
                count += 1
                last_time = res[i][2]
        return count
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends