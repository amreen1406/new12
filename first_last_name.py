# write a python program which accept the user's first and lat name and print them in reverse order with a space between them.



first_name = input(f"Enter the first name : " )
last_name = input(f"Enter the last name : " )
full_name = first_name +  "  " + last_name
#print(full_name)
reverse_name = full_name[::-1]
print(reverse_name)

