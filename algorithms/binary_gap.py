# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    found = 0
    longest_gap = 0

    print(binary)
    for i in binary:
        if i == '0':
            found += 1
        elif i == '1' and found > 0:
            longest_gap = max(found, longest_gap)
            found = 0
        print(found)
    return longest_gap

print("lg", solution(2500))
