'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(nums): # 0(n^2)
    # one possible first-pass solution
    # we'll keep an array, call it `no_dups` to hold numbers we see in the numbs array
    no_dups = [] # 0(n)

    # iterate through nums
    for num in nums: # 0(n)
        # check to see if the number is already in the `no_dups` array
        if num not in no_dups: # 0(n)
            no_dups.append(num)
        # if it is, remove it from the `no_dups` array
        else:
            no_dups.remove(num) # 0(n)
    # when we're done iterating, the only number in our `no_dups` array is the odd number out
    # return the odd number out
    return no_dups[0]



def single_number_optimized(nums): # 0(n)
    # keep track of number of times an item occurs in input
    counts = {}

    # loop through input list 0(n)
    for num in nums:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            counts[num] = 1
            # add item



        # # check if item is in counts
        # if num in counts:
        #     # if it is, increment the count
        #     num += 1
        # # if item is not in counts
        # else:
        #     # set item count to 1
        #     num = 1

    return counts[counts.keys()[0]]
    for k, v in counts.items(): # 0(n)
        if v == 1:
            return k




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")