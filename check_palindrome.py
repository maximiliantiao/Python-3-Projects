def check_palindrome(numbers):
    # Variable Declaration
    numbers_str = str(numbers)
    numbers_backwards = ""

    # Check input if contain any letters
    if (numbers_str.isalpha()):
        print("There is a letter in the input!")
    else:
        pass

    # Iterate backwards through input string
    count = len(numbers_str) - 1
    while (count >= 0):
        numbers_backwards += numbers_str[count]
        count -= 1

    # Check if input is a palindrome
    if (numbers_str == numbers_backwards):
        return "The number is a palindrome!"
    else:
        return "The number is not a palindrome!"


number_input = input("Enter a number: ")
print("\n")
print(check_palindrome(number_input))
print("\n")

yes_or_no = input("Want to input another number? (Y / N): ")
print("\n")

while (yes_or_no == 'Y' or yes_or_no == 'y'):
    number_input = input("Enter a number: ")
    print("\n")
    print(check_palindrome(number_input))
    print("\n")

    yes_or_no = input("Want to input another number? (Y / N): ")
print("\n")

