'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# first I am going to look and see if there is a python function that decides whether something is repeated

# for each number in the array, look and see if the number appears in the rest of the array sliced at the number
# if it does, delete both numbers
# if it doesn't, return the number

# using set:
# find a list of the intersecting numbers, remove them from the array, return the remaining number

def single_number(arr):
    # Your code here
    # for i in range(0,(len(arr)-1)):
    #     for j in range(i+1,(len(arr[i:]))):
    #         if arr[i] == arr[j]:
    #             item = arr[i]
    #             arr.remove(item)
    #             arr.remove(item)
    #             single_number(arr)
    # return(arr[0])
    for i in arr:
        if arr.count(i)==1:
            return i



 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")