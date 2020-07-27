def change(n, coins):
    combinations = [0 for index in range(0, n+1)]
    combinations[0] = 1
    for coin in coins:
        for index in range(1, n+1):
            if index >= coin:
                combinations[index] += combinations[index - coin]

    print(combinations[n])

n = 4
coins = [1,2,3]
coins = [5,10,15]
change(n, coins)