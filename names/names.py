import time
from borrowedBST import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# purpose, 

# we have a name_1 we are searching for in a pile of name_2

# lets put the array of names_2 in a binary search tree
g = BinarySearchTree(names_2[0])
names_2.pop(0)
for name in names_2:
    g.insert(name)

duplicates = []
for name in names_1:
    if g.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

