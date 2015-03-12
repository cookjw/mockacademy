def stock_picker(prices):
    maximum = 0
    days = [0,0]
    for buy_day in range(len(prices)):
        for sell_day in range(buy_day, len(prices)):
            if prices[sell_day] - prices[buy_day] > maximum:
                maximum = prices[sell_day] - prices[buy_day]
                days = [buy_day, sell_day]
    return days
    
prices = [1,2,-30,4,5,60,7]
print stock_picker(prices)