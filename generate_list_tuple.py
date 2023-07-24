

input_sequence = input("Enter a sequence from comma seperated number from  the user : " )

number_list = input_sequence.split(',')
number_tuple = tuple(number_list)

print ("list :" , number_list)
print ("tuple :" , number_tuple)
