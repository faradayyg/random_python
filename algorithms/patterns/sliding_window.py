"""
Given an array, we want to find the sum of all contiguous subarrays of a certain size.

I.E Given an array n of size 20 for example
we want to find the sum of all contiguous subarrays within this array.

There are two ways (I know of) to implement this:
1. Sliding window pattern,
2. Brute force iterative pattern
"""

from typing import List
import math


def brute_force_sum_of_contiguous(array, contingent_size):
    """Iterate over the array and add all contingents."""
    array_length = len(array)
    contiguous_sums = []

    for i in range(0, array_length - contingent_size + 1):
        contiguous_sum = 0
        for j in range(i, i+contingent_size):
            contiguous_sum += array[j]
        contiguous_sums.append(contiguous_sum)
    print(contiguous_sums)


def sliding_window_sum_of_contiguous(array, window_size):
    """Use the sliding window pattern to determine this

    Args:
        array (array): The array to be evaluated
        window_size (int): size of windows to find contiguous arrays
    """
    window_sum = 0
    contiguous_sums = []
    window_start = 0

    for window_end in range(0, len(array)):
        window_sum += array[window_end]

        if window_end >= window_size - 1:
            contiguous_sums.append(window_sum)
            window_sum -= array[window_start]
            window_start += 1
    print(contiguous_sums)

arr = [1,2,3,4,9,4,5]
c_s = 3

# sliding_window_sum_of_contiguous(arr, c_s)
# brute_force_sum_of_contiguous(arr, c_s)

"""Sum of smallest subarray whose sum is >= a number K
Given an array [1,4,6,8] k = 7
the answer here is 8 because 8 is the shortest subarray >= 7

Given another array [2, 1, 5, 2, 3, 2], K=7

the answer here is [5,2]
"""

def sliding_window_shortest_subarray_gt_val(array: List, K: int):
    """Sliding window."""
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(0, len(array)):
        window_sum += array[window_end]

        while window_sum >= K:
            min_length = min(min_length, (window_end - window_start + 1))
            print(array[window_start:window_end+1])
            print(window_start, window_end)
            window_sum -= array[window_start]
            window_start += 1
    print(min_length)


# sliding_window([1,4,6,8], 7)


"""Find the length of substring with no more than N distinct characters

Eg; Given a string "araabab" N = 2

Find the longest substring with no more than 2 different characters in them.

here: the answer is 4. I.E "araa"

Dynamic Sliding pattern
"""
def longest_substring_distinct(word, n):
    """Where n is the number of distinct characters."""
    chars = {}
    window_start = 0
    longest = 0

    for window_end, character in enumerate(word):
        c = chars.get(character, None)
        longest = max((window_end-window_start), longest)

        chars[character] = 1 if not c else c + 1

        while(chars[character] > n):
            print("got here for", character)
            char_at_win_start = word[window_start]
            chars[char_at_win_start] -= 1
            if chars[char_at_win_start] <= 0:
                del chars[char_at_win_start]
            window_start += 1


    print(longest, chars)

# longest_substring_distinct("araabab", 2)


"""
Given a string of lowercase characters, and you are allowed
to replace not more than k characters, find the longest substring after replacement

Eg: aabbccbb

Ans: 5 because replacing "cc" with b would create 5 in length substring
and that would be the longest

Technique: Dynamic sliding window
"""

def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
        max_repeat_letter_count, frequency_map[right_char])
        print(frequency_map)

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length

print(length_of_longest_substring("abccde", 1))



def longest_substring_without_repeating(st: str):
    longest = 0
    start = 0
    found = {}
    for i, ch in enumerate(st):
        char_instances = found.get(ch, 0)
        found[ch] = char_instances + 1
        while found[ch] >1:
        # move left window up one level
            left_char = st[start]
            found[left_char] -= 1
            start += 1

        longest = max(longest, i-start + 1)

    return longest

# print(longest_substring_without_repeating("pwwkeow"))
