'''
Input: a List of integers
Returns: a List of integers
'''
#given array of integers
# returns array
# each index in new array is the product of each other number in array

# when iterating over the input array, the expected value at the current
# iteration index, needs to be the product of every number except at the current iteration index

def product_of_all_other_numbers(arr):
    # Your code here
    
    # for each num in array
    # multiply all nums in array and divide by current index

    # create empty list to store totals
    newArray = []

    # for each num in array 
    for i in range(0, len(arr)):
        # set total to 1
        total = 1
        # for each num in array 
        for j in range(0, len(arr)):
        #  if urrent index of 1st loop isn't the same of index of 2nd loop
            if i != j:
                # multiply each value by total number
                total *= arr[j]
        # add that total to the new array
        newArray.append(total) 
    # return new array
    return newArray



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
