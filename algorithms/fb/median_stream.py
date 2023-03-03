import math
from heapq import heappop, heappush
# Add any extra import statements you may need here


# Add any helper functions you may need here
def add_number(bottom, top, num):
  heappush(bottom, -num)
  heappush(top, -(heappop(bottom)))

  if len(top) > len(bottom):
    heappush(bottom, -(heappop(top)))


def get_med(top, bottom):
  if len(top) == len(bottom):
    return (-bottom[0] + top[0]) // 2
  else:
    return -bottom[0]

def findMedian(arr):
  bottom = []
  top = []
  medians = []

  for i in arr:
    add_number(bottom, top, i)
    medians.append(get_med(top=top, bottom=bottom))
  return medians













# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here