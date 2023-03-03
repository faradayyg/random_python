# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    new_array = [None] * len(A)
    for i in range(len(A)):
        new_index = (i + K) % len(A)
        new_array[new_index] = A[i]
    return new_array
print(solution([1,2,3], 2))


