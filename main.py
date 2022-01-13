
with open("file1.txt") as file1:
    list1 = file1.readlines()
    new_list1 = [n.strip() for n in list1]
    print(new_list1)

with open("file2.txt") as file2:
    list2 = file2.readlines()
    new_list2 = [n.strip() for n in list2]
    print(new_list2)

# Write your code above 👆

result = [num for num in new_list1 if num in new_list2]

print(result)

