import time

name = raw_input("Hello! What is your name?\n")

#time.sleep(1)

print("\nHello " + name + "! My name is Charles the Calculator!")
	
#time.sleep(3)
	
count = 0

while count < 10:

	print("\nPlease type in two number.")

	number1 = raw_input("\nFirst number: \n")
	while number1.isalpha() == True:
		print("Please enter a number!")

		number1 = raw_input("\nFirst number: \n")
	number2 = raw_input("Second number: \n")

	while number2.isalpha() == True:
		print("Please enter a number!")
		number2 = raw_input("Second number: \n")

	print("What operation?")
	operator = raw_input("Add	Subtract	Multiply	Divide\n")

	int1= int(number1)
	int2 = int(number2)

	if operator == "add" or operator == "Add":
		print(\nint1 + int2)
	elif operator == "subtract" or operator == "Subtract":
		print(\nint1 - int2)
	elif operator == "multiply" or operator == "Multiply":
		print(\nint1 * int2)
	elif operator == "divide" or operator == "Divide":
		print(int1 / int2)
	else:
		print("\nInvalid operator!")

	count += 1

