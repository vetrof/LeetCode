# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8


def maximumWealth(accounts):
    for n, i in enumerate(accounts):
        accounts[n] = sum(i)
    return max(accounts)


accounts = [[1, 5], [7, 3], [3, 5]]
print(maximumWealth(accounts))

