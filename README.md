# Stock Maximize

## Problem Description

This program solves the Stock Maximize problem from HackerRank. The challenge is to determine the maximum profit that can be obtained from buying and selling stocks, given a predicted set of stock prices for the next several days.

## Algorithm

The solution uses a greedy approach with reverse iteration:

1. Iterate through the prices array from right to left.
2. Keep track of the maximum price seen so far.
3. For each price:
   - If it's higher than the max price, update the max price.
   - If it's lower, add the difference (profit) to the total.

This approach ensures maximum profit by:
- Always selling at the highest future price.
- Buying on any day where the price is lower than a future selling price.

## Implementation

The core function `stockmax(prices)` takes an array of predicted stock prices and returns the maximum possible profit.

```python
def stockmax(prices):
    max_price = 0
    total_profit = 0
    
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            total_profit += max_price - price
    
    return total_profit
