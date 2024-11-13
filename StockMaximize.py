'''
Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. 
(WOT) will be for the next number of days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. 
What is the maximum profit you can obtain with an optimum trading strategy?

Example

prices = [1,2]

Buy one share day one, and sell it day two for a profit of 1. Return 1.

prices = [2,1]

No profit can be made so you do not buy or sell stock those days. Return 0.

*****Function Description*****

Complete the stockmax function in the editor below.

stockmax has the following parameter(s):

prices: an array of integers that represent predicted daily stock prices
Returns

int: the maximum profit achievable
Input Format

The first line contains the number of test cases .

Each of the next  pairs of lines contain:
- The first line contains an integer , the number of predicted prices for WOT.
- The next line contains n space-separated integers , each a predicted stock price for day .


****Constraints****
    1<=t<=10
    1<=n<=5000
    1<=prices[i]<=10000


Output Format

Output t lines, each containing the maximum profit which can be obtained for the corresponding test case.

Sample Input

STDIN       Function
-----       --------
3           q = 3
3           prices[] size n = 3
5 3 2       prices = [5, 3, 2]
3           prices[] size n = 3
1 2 100     prices = [1, 2, 100]
4           prices[] size n = 4
1 3 1 2     prices =[1, 3, 1, 2]
Sample Output

0
197
3
Explanation

For the first case, there is no profit because the share price never rises, return 0.
For the second case, buy one share on the first two days and sell both of them on the third day for a profit of 197.
For the third case, buy one share on day 1, sell one on day 2, buy one share on day 3, and sell one share on day 4. 
The overall profit is 3.'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    max_price = 0
    total_profit = 0
    
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            total_profit += max_price - price
    
    return total_profit
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
