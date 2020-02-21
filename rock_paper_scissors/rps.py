#!/usr/bin/python

import sys



def rock_paper_scissors(n):
  result = []
  plays = ['rock', 'paper', 'scissors']

  def rps_helper(n, rounds=[]):
    if n == 0:
      return result.append(rounds)
    else:
      for play in plays:
        # rounds = rounds + [play]
        # print(f'rounds', rounds)
        print(f'play', n, play, rounds)
        rps_helper(n - 1, rounds + [play])
  
  rps_helper(n)
  print(f'result', result)
  return result





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')