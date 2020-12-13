def solve(arr):
    evenptr = 0
    oddptr = len(arr) - 1
    while evenptr < oddptr:
        if arr[evenptr] % 2 == 0:
            evenptr += 1
        else:
            arr[evenptr], arr[oddptr] = arr[oddptr], arr[evenptr]
            oddptr -= 1

    return arr

inp = [4,9,5,2,9,5,7,10]
print(solve(inp))

#10,4,2,5,9,5,7,9