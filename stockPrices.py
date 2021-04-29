def get_max_profits(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError("Getting a profit requires at least two prices")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        print(current_time, "currenttime")
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]
print("max profit is:", get_max_profits(stock_prices))
