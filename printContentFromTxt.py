welcome_msg = "Welcome to Text Stats, a program that shows you stats about your texts"
decorator = "-" * len(welcome_msg)

print(decorator + "\n")
print(welcome_msg + "\n")
print(decorator)
print("\nWhich do you wish to see: \n")
print("A. # of characters with spaces\n")
print("B. # of characters without spaces\n")
print("C. # of lines in your document (Still needs word)\n")
print(decorator + "\n")

user_mode = input("Enter mode: ")
print("\n")

number_of_char_in_contents = 0

my_file = open("C Programming.txt", "r")

contents_read = my_file.read()
contents_readline = my_file.readline()


if (user_mode == "A" or user_mode == "a"):
    for char in contents_read:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;',./{|}:<>?\" ":
            number_of_char_in_contents += 1
        else:
            number_of_char_in_contents += 0

    print("This text file has " + str(number_of_char_in_contents) + " characters with spaces!\n\n")

elif (user_mode == "B" or user_mode == "b"):
    for char in contents_readline:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;',./{|}:<>?\"":
            number_of_char_in_contents += 1
        else:
            number_of_char_in_contents += 0

    print("This text files has " + str(number_of_char_in_contents) + " characters without spaces!\n\n")
elif (user_mode == "C" or user_mode == "c"):
    count = 0
    while contents_readline:
        count += 1
        contents_readline = my_file.readline()
    
    print(count)

my_file.close()