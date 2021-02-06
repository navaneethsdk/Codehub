def gridTraveller(m,n,memo={}):
    """
    number of ways to travel an m x n grid.
    Essentially if k1,k2 is our current coordinate (starting from m,n)
    in the grid we only have to consider a grid of k1 x k2 in the next recursion
    Brute force: TC = O(2^m*n) SC = O(m+n)
    Memoization: TC = O(m*n) SC = O(m+n)
    """
    key = str(m)+","+str(n)
    if key in memo:return memo[key]
    if m==0 or n==0: return 0
    if m==1 and n==1: return 1
    memo[n] = gridTraveller(m-1,n) + gridTraveller(m, n-1) 
    return memo[n]

if __name__ == "__main__":
    gridTraveller(1,1)
    gridTraveller(1,1)
    gridTraveller(1,1)
    gridTraveller(1,1)