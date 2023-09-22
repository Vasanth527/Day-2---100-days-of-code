# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))
a = two_digit_number[0]
b = two_digit_number[1]
a1 = int(a)
b1 = int(b)
print(a1 + b1)

# type = int(a) / type = str(a) type conversion
# print(type(a)) = type check
# [0],[1] = substring

# ANGELA CODE

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
two_digit_number = first_digit + second_digit

print(two_digit_number)
