
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
# for name_1 in names_1:
#     names.append(name_1)

# names_1.sort()

# def re_check_dupes(val, search_arr):

#     center = len(search_arr) - 1 // 2
#     if val == search_arr[center]: return True

#     left = search_arr[:center]
#     right = search_arr[center + 1:]

#     if val > center:
#         return re_check_dupes(val, right)

#     elif val < center:
#         return re_check_dupes(val, left)

#     return False

# for i in names_2:
#     if re_check_dupes(i, names_1):
#         names.append(i)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:

            if self.left is None:
                self.left = BST(value)
                return
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                return
            else:
                self.right.insert(value)

    def contains(self, value):

        if self.value == value: return True

        elif value < self.value:

            if self.left is None: return False

            else:
                return self.left.contains(value)

        else:

            if self.right is None: return False

            else:
                return self.right.contains(value)

bst = BST(names_1[0])
if bst.value > names_1[1]:
    print('true')

for i in range(1, len(names_1)):
    bst.insert(names_1[i])

for i in names_2:
    if bst.contains(i):
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.