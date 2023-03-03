"""
Initiates two pointers which loop through a linear
data structure in a single iteration (arguably)

Eg use cases can be: finding a palindrome, sum of three numbers


I currently feel like it can also be used in almost the same way sliding window is used.
"""


def palindrome(input):
    print(input)
    low = 0
    high = len(input) - 1

    while low < high:
        if input[low] == input[high]:
            low += 1
            high -= 1
        else:
            return False
    return True


def palindromeII(s):
    mismatches = start = 0
    end = len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif mismatches == 0:
            return any([palindrome(s[start:end]), palindrome(s[start+1:end+1])])
        else:
            return False
    return True




def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    pairs = []
    print(nums)
    for i, value in enumerate(nums):
        if i > 0 and value == nums[i-1]:
            continue
        low_index = i + 1
        high_index = len(nums) - 1
        while low_index < high_index:
            three = (value, nums[low_index], nums[high_index])

            three_sum = sum(three)
            print("three ", three, "=", three_sum)

            if three_sum == 0:
                pairs.append([value, nums[low_index], nums[high_index]])
                low_index += 1
                high_index -= 1

                while nums[low_index] == nums[low_index - 1] and low_index < high_index:
                    low_index += 1
                while nums[high_index] == nums[high_index + 1] and low_index < high_index:
                    high_index -= 1
            elif three_sum < 0:
                low_index += 1
            elif three_sum > 0:
                high_index -= 1

    return pairs


def reverse_words(sentence):
   # write you code
    def str_rev(strings: list[str], start, end):
        while start < end:
            strings[start], strings[end] = strings[end], strings[start]
            start +=1
            end -= 1
        return strings

    reversed = str_rev([i for i in sentence], 0, len(sentence) - 1)
    new = []

    start = 0
    end = 1

    while start < end:
        if reversed[start] != " " and reversed[end] != " ":
            end += 1
        if reversed[end] == " ":
            new.append(str_rev(reversed, start, end))
            print(new)
            start = end
            end += 1


reverse_words("Hello World!")
# print(three_sum([-2,0,0,2,2]))
# print(palindromeII("madame"))