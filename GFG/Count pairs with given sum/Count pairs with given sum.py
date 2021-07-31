def getPairsCount(self, arr, n, sum):
        m = dict()
 
        # Store counts of all elements in map m
        for i in range(n):
            if arr[i] in m.keys():
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
 
        twice_count = 0
 
        # Iterate through each element and increment
        # the count 
        for i in range(0, n):
            if (sum-arr[i]) in m.keys():
                twice_count += m[sum - arr[i]]
 
            # if (arr[i], arr[i]) pair satisfies the
            # condition, then we need to ensure that
            # the count is  decreased by one such
            # that the (arr[i], arr[i]) pair is not
            # considered
            if (sum - arr[i] == arr[i]):
                twice_count -= 1
 
        # return the half of twice_count
        return int(twice_count / 2)