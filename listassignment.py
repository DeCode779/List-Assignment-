# 1. Create an empty list
my_list=[]

# 2. Append the following element; 10, 20, 30, 40
my_list.append(10)
my_list.append(20)      
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# 3. Insert the value 15 at the second position
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# 4. Extend my list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# 5. Remove the last element from my_list
my_list.pop()
print("After popping the last element:", my_list)

# 6. Sort my_list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)