"""
Rotational Cipher
Zebra-493 Rotated by a Factor of 3 becomes:
Cheud-726.
"""

def rotate(st, k, char_set):
    index = char_set.find(st)
    new_index = index + k
    old_n = new_index
    new_index = new_index if new_index < len(char_set) else new_index % len(char_set)
    print(new_index, old_n)
    return char_set[new_index]


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def rotate(st, k, char_set):
    index = char_set.find(st)
    new_index = index + k
    new_index = new_index if new_index < len(char_set) else new_index % len(char_set)
    return char_set[new_index]

def rotationalCipher(st, k):
  # Write your code here
    import string
    all_possible_lower_alphabets = string.ascii_lowercase[:26]
    all_possible_upper_alphabets = string.ascii_uppercase[:26]
    all_possible_numbers = "0123456789"

    for j,s in enumerate(st):
        if s in all_possible_lower_alphabets:
            st = st[:j] + rotate(s, k, all_possible_lower_alphabets) + st[j+1:]
        elif s in all_possible_numbers:
            st = st[:j] + rotate(s, k, all_possible_numbers) + st[j+1:]
        elif s in all_possible_upper_alphabets:
            st = st[:j] + rotate(s, k, all_possible_upper_alphabets) + st[j+1:]
        else:
            st = st[:j] + s + st[j+1:]
        
    return st











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here


print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
