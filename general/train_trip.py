def count_ways(n): 
    """
    To count number of ways 
    one can move from A to B
    """
    if n==0:
        return 1
    elif n==1:
        return 2
    elif n==2:
        return 3

    edges = [0 for i in range(0, n + 1)] 

    # base cases 
    edges[0] = edges[1] = 1
    edges[2] = 2
    edges[3] = 4

    # Iterate from 4 to n 
    for i in range(4, n + 1): 
        edges[i] = edges[i - 1] + edges[i - 2] + edges[i - 3] 

    return edges[-1] 
  
      
# Driver code  
if __name__ == "__main__":
    n = int(input())
    while(n > 0):
        stations = int(input())
        print(count_ways(stations))
        n-=1