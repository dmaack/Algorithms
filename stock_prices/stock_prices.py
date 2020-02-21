#!/usr/bin/python

import argparse
# iterate over prices
# keep track of current min price so far
# keep track of max profit so far
# return max profit
def find_max_profit(prices):

  cur_min_price_so_far = prices[0] # 100
  max_profit_so_far = prices[1] - prices[0] # 90 - 100 = -10

      #90
  for i in range(1, len(prices)): 
    profit = prices[i] - cur_min_price_so_far # 90 - 100 = -10

    if prices[i] < cur_min_price_so_far: 
      cur_min_price_so_far = prices[i]
    
    if profit > max_profit_so_far: # -10 > -10
      max_profit_so_far = profit # -10

  return max_profit_so_far
# print(find_max_profit(prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))