class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        
        ans = arr[n-1] - arr[0]
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            smallest = min(arr[0] + k, arr[i] - k)
            largest = max(arr[i-1] + k, arr[n-1] - k)
            
            ans = min(ans, largest - smallest)
        
        return ans
