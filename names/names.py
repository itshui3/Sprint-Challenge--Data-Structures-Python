import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
# Split up by line into columns
f.close()
# print(names_1, 'names 1')
f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1: # Iterate through 1st list of names
#     for name_2 in names_2: # Within each iteration^ iterate through 2nd list of names
#         if name_1 == name_2: # Compare and append the names into a duplicates array
#             duplicates.append(name_1)
names_2 = sorted(names_2)
for name_1 in names_1: # Iterate through 1st list of names
    names = names_2
    start = 0
    end = len(names_2)-1
    while len(names):
        start = 0
        end = len(names)-1
        mid = (end - start)//2
        if names[mid] == name_1:
            duplicates.append(name_1)
            break
        elif name_1 > names[mid]:
            start = mid + 1
            names = names[mid + 1:]
            continue
        elif name_1 < names[mid]:
            end = mid - 1
            names = names[:mid]
            continue
        else:
            break

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
