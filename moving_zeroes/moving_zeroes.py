'''
Input: a List of integers
Returns: a List of integers
'''
# given an unsorted array of integers
# move all non 0s to the left of 0
# return the updated array

# what if no 0's?; return unaltered array

def moving_zeroes(arr):
    # Your code here

    # loop through each num in array
    # if num is not 0 put in 1st array 
    # if num is 0 put in 2nd array 
    # combine the arrays
    newArr = [num for num in arr if num != 0] + [num for num in arr if num == 0]
    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")