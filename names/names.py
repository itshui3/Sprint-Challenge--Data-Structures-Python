
import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
names = []

names_1.sort()

def re_binary_search(arr, target):
    # search an array for a value in O(log n)
    # return True if it is found in given array
    # return False if it is not found

# R_i
    if len(arr) < 2:
        if target == arr[0]: return True
        else: return False
# R_ie_1
    elif len(arr) % 2 == 0:
        # even
        middex_right = len(arr) // 2
        middex_left = middex_right - 1

        if target == arr[middex_right] or target == arr[middex_left]: return True
        elif target > arr[middex_left] and target < arr[middex_right]: return False

        elif target < arr[middex_left]:
            # recurse with left_arr, inclusive middex_left
            left_arr = arr[:middex_left+1]
            return re_binary_search(left_arr, target)

        elif target > arr[middex_right]:
            # recurse with right_arr, inclusive middex_right
            right_arr = arr[middex_right:]
            return re_binary_search(right_arr, target)

# R_e
    else:
        # odd
        middex = len(arr) // 2
        
        if target == arr[middex]: return True
        elif target < arr[middex]:
            # recurse with left_arr
            left = arr[:middex]
            return re_binary_search(left, target)
        elif target > arr[middex]:
            # recurse with right_arr
            right = arr[middex+1:]
            return re_binary_search(right, target)

for i in names_2:
    if re_binary_search(names_1, i):
        duplicates.append(i)
    # in binary search with an array, there are two cases to watch out for
    # 1st is if the leftover array is an odd number of elements
    # in this case, the middle is a single element

    # 2nd case is if there are an even number of elements
    # in this case, 
    # the floor division of length of arr // 2
    # the mid is the first element on the right side 



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.