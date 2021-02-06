def fib(n, memo={}):
    """
    recursive function to find nth fibinocci number
    time complexity : O(2^n) -> O(n)
    space complexity : O(n) hint: count no of stack frames
    """
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

if __name__ == "__main__":
    print(fib(50))