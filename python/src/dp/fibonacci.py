# Solve fibinacci series with DP

## Memoization Botton up
def fibonacciWithDP(n):
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(fibonacciWithDP(1))
print(fibonacciWithDP(2))
print(fibonacciWithDP(7))
print(fibonacciWithDP(9999))

# Memoization Top down
def fibonacciWithDP_TD(n):
    if ( memo[n] == -1 ):
        if( n <= 1 ):
            memo[n] = n
        else:
            memo[n] = fibonacciWithDP_TD(n-1) + fibonacciWithDP_TD(n-2)

    return memo[n]

## Top Down set default value
fib = 7
memo = [-1] * (fib+1)
print(fibonacciWithDP_TD(fib))
