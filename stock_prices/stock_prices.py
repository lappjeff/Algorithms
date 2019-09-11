#!/usr/bin/python

import argparse


prices = [100, 90, 80, 50, 20, 10]


#min number is the best buying price
#max number is the best selling price

#min number can only check items that come at a higher index in list - represents time
def find_max_profit(prices):


    max_profit_so_far = prices[1] - prices[0]

    #loop through all prices except last one
    # we dont need the last one because there is nothing to the right of it to compare against
    for i in range(len(prices) - 2):
        for j in range(i + 1, len(prices) - 1):
            profit = prices[j] - prices[i]

            if profit > max_profit_so_far:
                max_profit_so_far = profit

    return max_profit_so_far
find_max_profit(prices)

# find_max_profit([10, 7, 5, 8, 11, 9]) === 6
# 10 is set as current_min_price_so_far
# 10 is subtracted from  every following index value to determine a new max_profit_so_far

# 7 - 10 = -3 - max_profit_so_far = -3
# 5 - 10 = -5 - max_profit_so_far = -3
# 8 - 10 = -2 - max_profit_so_far = -2
# 11 - 10 = 1 - max_profit_so_far = 1
# 9 - 10 = -1 - max_profit_so_far = 1

#increment index to 1
#7 is less than 10, so current_min_price_so_far = 7
# 7 is subtracted from every following index value to determine a new max_profit_so_far

# 5 - 7 = -2 -- max_profit_so_far = 1
# 8 - 7 = 1 -- max_profit_so_far = 1
# 11 - 7 = 4 -- max_profit_so_far = 4
# 9 - 7 = 2 -- max_profit_so_far = 4

#increment index to 2
#5 is less than 7, so current_min_price_so_far = 5
# 5 is subtracted from every following index value to determine a new max_profit_so_far

# 8 - 5  = 3 -- max_profit_so_far = 4
# 11 - 5  = 6 -- max_profit_so_far = 6
# 9 - 5   = 4 -- max_profit_so_far = 6

# if no new current_min_price_so_far is found, 6 is the max_profit_so_far and should be returned

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
