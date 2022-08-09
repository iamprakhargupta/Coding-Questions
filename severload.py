# def serverload(n,arr):
#     loadtol=sum(arr)
#     load=loadtol//2
#     dp=[]
#     for i in range(n+1):
#         x=[0]*(load+1)
#         dp.append(x)
#
#     print(dp)
#
# serverload(2,[1, 2, 3, 4, 5])

def minServerLoads(n, servers):
    # Compute the overall server load
    totalLoad = sum(servers)

    requiredLoad = totalLoad // 2

    # Stores the results of subproblems
    dp = [[0 for col in range(requiredLoad + 1)]
          for row in range(n + 1)]

    # Fill the partition table
    # in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, requiredLoad + 1):

            # If i-th server is included
            if servers[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

            # If i-th server is excluded
            else:
                dp[i][j] = max(dp[i - 1][j],
                               servers[i - 1] +
                               dp[i - 1][j - servers[i - 1]])
    for i in dp:
        print(i)
    # Server A load: total_sum-ans
    # Server B load: ans
    # Diff: abs(total_sum-2 * ans)
    return totalLoad - 2 * dp[n][requiredLoad]


# Driver Code

N = 2;

servers = [1, 2,4]

# Function Call
print(minServerLoads(N, servers))