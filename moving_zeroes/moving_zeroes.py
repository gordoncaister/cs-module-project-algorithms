'''
Input: a List of integers
Returns: a List of integers
'''
#   use python sort method to sort numbers, based on their positive value, in descending order

def moving_zeroes(arr):
    arr.sort(reverse=True, key=sortfunc) #reverse=True = descending order, key= a function to specify the sorting criteria
    return arr
# this function returns the element by its absolute (positive) value
def sortfunc(e):
    return abs(e)




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")