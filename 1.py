# Taking four inputs and converting them into different data structures
input_1 = input("Enter the first value: ")
input_2 = input("Enter the second value: ")
input_3 = input("Enter the third value: ")
input_4 = input("Enter the fourth value: ")

# Converting inputs into different data structures
my_list = [input_1, input_2, input_3, input_4]
my_tuple = (input_1, input_2, input_3, input_4)
my_set = {input_1, input_2, input_3, input_4}
my_dict = {
    "value_1": input_1,
    "value_2": input_2,
    "value_3": input_3,
    "value_4": input_4
}

print("\nOriginal Data Structures:")
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

# Taking the fifth input and adding it to the data structures
input_5 = input("\nEnter the fifth value: ")

my_list.append(input_5)
my_tuple = my_tuple + (input_5,)
my_set.add(input_5)
my_dict["value_5"] = input_5

print("\nData Structures After Adding Fifth Input:")
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
