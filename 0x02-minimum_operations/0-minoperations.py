#!/usr/bin/python3

def minOperations(n):
  """
  write a  method that calculates the fewest number of operations
  needed to result in exactly n H characters in the file.
  Prototype: def minOperations(n)
  Returns an integer
  If n is impossible to achieve, return 0
  """
  if n <= 1:
    return 0

  for e in range(2, (int(n/2)+1)):
    if n % e == 0:
      return minOperations(int(n/e)) + e
  return n
