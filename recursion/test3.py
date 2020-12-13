def ispossible(arr, k):
    return helper(0, arr, k, False)

def helper(ri, arr, remaining, picked):
    if ri >= len(arr):
        if picked and remaining == 0:
            return True

    print(remaining)
    helper(ri+1, arr, remaining-arr[ri], True)
    
    #return helper(ri+1, arr, remaining-arr[ri], True)


inp = [1, 2, 3]
print(ispossible(inp, 5))