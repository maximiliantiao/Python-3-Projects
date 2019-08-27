number_of_char_in_contents = 0

my_file = open("Allerio Colors.txt", "r")

contents = (my_file.read())

for char in contents:
    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;',./{|}:<>?\"":
        number_of_char_in_contents += 1
    else:
        number_of_char_in_contents += 0

print(number_of_char_in_contents)

my_file.close()