def stock_buy_sell(a):
    maxp = 0
    minp = float('inf')
    for i in range(len(a)):
        minp = min(minp, a[i])
        maxp = max(maxp, a[i]-minp)
    return maxp


# a = [7, 1, 5, 3, 6, 4]
a = [7, 6, 4, 3, 1]
print(stock_buy_sell(a))