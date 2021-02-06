def canSum(targetSum,numbers,memo={}):
    """
    program to find  whether an array of numbers can 
    derive derive a target number through addition operation
    Time complexity : O(n^m)->O(n*m);   n:length of array, m: target
    Space Complexity : O(m)
    """
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder,numbers,memo)==True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False
        
if __name__ == "__main__":
    print(canSum(7,[2,3]))
    print(canSum(16,[5,7]))