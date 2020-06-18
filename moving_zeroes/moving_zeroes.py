'''
Input: a List of integers
Returns: a List of integers
'''

# [0,0,0,1,2,3] --return--> [1,2,3,0,0,0]

# two pointers?

'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?

if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap

if the left sees a non-zero increment
if the right sees a zero increment
'''

def moving_zeroes(arr): # 0(n^n)
    # loop through each item of input list
    for i in range(len(arr)): # 0(n)
        x = arr[i]
        # if the item is non-zero
        if x != 0:
            # extract from the list and place at the beginning
            arr = [x] + arr[:i] + arr[i+1:] # 0(n)

    return arr

# def moving_zeroes(arr):
    # left pointer at the beginning
    # right pointer at the end

    # loop until left and right pointers meet or right pointer passes the left pointer
        # swap situation:
        # left sees zero and right sees non-zero
            # swap the items
            # increment left
            # decrement right
        # non-swap situation
            # if left sees non-zero
                # increment left
            # if right sees zero
                # decrement right
    # return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")