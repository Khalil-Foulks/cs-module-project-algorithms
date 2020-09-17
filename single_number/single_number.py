'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# given array of integers
# array will NEVER be empty
# every element appears twice except 1
# RETURN that single number


# def single_number(arr):
# # runtime O(n^2)

#     # for each item in the array
#     for i in arr: # O(n)
#     # count if the current item appears in the array
#         if arr.count(i) == 1: # O(n)
#     # return the num that isn't duplicated
#             return i

# O(n)
def single_number(arr):
    # sets are a closely-related cousin to dicts 
    # they don't associate values with keys 
    # they're useful for when you need the uniqueness
    # property of dicts
    s = set()
    # s = []

    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)
    # at this point, the only element in the set 
    # is our odd-element-out
#    return list(s)[0] # O(1)
    return s.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")