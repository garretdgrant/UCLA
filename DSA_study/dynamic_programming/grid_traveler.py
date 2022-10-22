def grid_traveler(m,n, memo = {}):
    """Takes in a size of a grid,
    returns the number of ways to get from (0,0)
    to (m,n)
    """
    if (m, n) in memo or (n,m) in memo: return memo[(m,n)]
    if m==1 and n == 1: return 1
    if m==0 or n == 0: return 0
    memo[(m,n)] = memo[(n,m)] = grid_traveler(m-1, n) + grid_traveler(m, n-1)
    return memo[(m,n)]

print(grid_traveler(1,1))
print(grid_traveler(2,3))
print(grid_traveler(3,3))
print(grid_traveler(18,18))
print(grid_traveler(50,50))

