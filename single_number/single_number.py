'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# given array of integers
# array will NEVER be empty
# every element appears twice except 1
# RETURN that single number



def single_number(arr):
    # Your code here

    # for each item in the array
    for i in arr:
    # count if the current item appears in the array
        if arr.count(i) == 1:
    # return the num that isn't duplicated
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")