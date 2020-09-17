'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# given an array of integers
# given window size, k
# window moves from left side of array to right side
# window moves one element at a time
# return max value of each window inside an array


def sliding_window_max(nums, k):
    # Your code here

    # create empty array to store max values
    max_values = []
    # create start for window
    start = 0
    # create end for window
    end = 0
    # stopping number for loop range
    stop = len(nums) - k + 1


    # for each num in the array
    for num in range(0, stop):
    # slice the input array using start and end
        window = nums[start:k + end]
    # find the max value inside window
        max_num = max(window)
    # append max value to empty array
        max_values.append(max_num)
    # increment starting position of window
        start += 1
    # increment ending position of window
        end += 1
    # repeat until (i * -1) == -k
    return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
