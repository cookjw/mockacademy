def find_max_profit_days(prices):
    results = []
    max_candidate = 0    
    for reference_day in range(len(prices)-1):
        for current_day in range(reference_day+1, len(prices)):
            profit = prices[current_day] - prices[reference_day]
            if profit > max_candidate:
                results = [(reference_day, current_day)]
                max_candidate = profit
            elif profit == max_candidate:
                results.append((reference_day, current_day))
    return (results, max_candidate)