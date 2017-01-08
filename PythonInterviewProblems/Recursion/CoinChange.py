# Greedy solutions
def rec_coin(target,coin):
    
    coin.sort(reverse=True)

    if target == 0:
        return 0

    num_largest_coins = target // coin[0]
    remainder = target % coin[0]
    
    if len(coin) > 0:
        coin.remove(coin[0])
    
    if remainder > 0:
        return num_largest_coins + rec_coin(remainder, coin)
    

    return num_largest_coins + rec_coin(remainder, coin)

# Greedy solutions
def rec_coin2(target,coin):

    if target == 0:
        return 0

    this_coin = coin.pop()

    num_largest_coins = target // this_coin
    remainder = target % this_coin

    if remainder > 0:
        return num_largest_coins + rec_coin2(remainder, coin)

    return num_largest_coins

# try for a non greedy solution
target = 63
coins = [2,5,10,20,50]
results = [0] * (target+1)

def rec_coin3(target, coins, results):
    
    min_coins = target // min(coins)
    
    # base case
    if target in coins:
        results[target] = 1
        return 1
    elif results[target] > 0:
        return results[target]

    for item in [c for c in coins if c <= target]:

        num_coins = 1 + rec_coin3(target - item, coins, results)

        if num_coins < min_coins and target - item >= 0:
            min_coins = num_coins
            results[target] = min_coins

    return min_coins

# print(rec_coin(19,[1,5]))
# print(rec_coin2(69,[1,5,10,25,50]))
# print(rec_coin2(63,[1,5,10,25]))
print(rec_coin3(target,coins, results))
print(results)