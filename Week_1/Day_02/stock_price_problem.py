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


def list_increasing_sequences(prices):
    results = []
    starting_index = 0
    current_index = 1
    while current_index <= len(prices) - 1:
        if prices[current_index] >= prices[starting_index]:
            if current_index < len(prices) - 1:
                current_index += 1
            else:
                results.append((starting_index, current_index))
                return results
        else:
            if current_index < len(prices) - 1:
                results.append((starting_index, current_index-1))
                starting_index = current_index
                current_index = starting_index + 1
            else:
                return results
    return results
    
def find_max_profit(prices):
    increasing_sequences = list_increasing_sequences(prices)
    profits = []
    for pair in increasing_sequences:
        profits.append(prices[pair[1]] - prices[pair[0]])
    return sum(profits)