import sys

def tiling():
    dp = [0 for _ in range(251)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3

    for i in range(len(dp)):
        if i > 2:
            dp[i] = dp[i-2] * 2 + dp[i-1]
    return dp

dp = tiling()

while True:
    try:
        target = int(sys.stdin.readline().strip())
        print(dp[target])
    except:
        break