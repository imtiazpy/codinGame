def leonardo(n):
    if n < 0:
        return "Error: n must be a non-negative integer."
    
    # Initialize array to store Leonardo numbers
    L = [0] * (n+1)
    
    # Base cases
    L[0] = 1
    L[1] = 1
    
    # Iterate through the array and compute Leonardo numbers using the recurrence relation
    for i in range(2, n+1):
        L[i] = L[i-1] + L[i-2] + 1
    
    # Return the n-th Leonardo number
    return L[n]


# bad solution, takes a long time for big input
# def leonardo(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return leonardo(n-1) + leonardo(n-2) + 1


n = int(input())

print(leonardo(n))