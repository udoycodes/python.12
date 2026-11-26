#Length of a first name
first_name= "Abed"
print(len(first_name))

#Compare two strings
first_name= "Abed"
last_name= "Rahman"
if first_name > last_name:
    print("First name is greater than last name.")
else:
    print("Last name is greater than first name.")

#Declare 5 as num_one and 4 as num_two
num_one= 5
num_two= 4

#Add num_one and num_two and assign the value to a variable total
total =num_one + num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one- num_two
print(diff)

#Multiply num_one and num_two and assign the value to a variable product
product= num_one *num_two
print(product)

#Divide num_one by num_two and assign the value to a variable division
division =num_one/ num_two
print(division)

#Modulus of num_one and num_two and assign the value to a variable remainder
remainder = num_one % num_two
print(remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp= num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

# Circle with radius 30 meters
radius = 30
pi = 3.14

#Area of a circle
area= pi*radius **2
print(area)

#Circumference of a circle
circumference= 2* pi * radius
print(circumference)

#radius from user input
radius= float(input("Enter radius: "))
area = pi *radius **2
print(f"The area of a circle with radius {radius} is: {area}")

#User input 
first_name= input("Enter your first name: ")
last_name= input("Enter your last name: ")
country= input("Enter your country: ")
age= input("Enter your age: ")

#keywords
help('keywords')