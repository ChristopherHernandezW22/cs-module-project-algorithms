#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#   # Your code here

#   pass

def rock_paper_scissors(n):
  result_array = []
  selection = ['rock', 'paper', 'scissors']

  def recursive_listing(iterations, result=[]):

    # Set base case
    if iterations == 0:
      return result_array.append(result)
    for choice in selection:
      recursive_listing(iterations -1, result + [choice])

  recursive_listing(n)
  return result_array

rock_paper_scissors(2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')