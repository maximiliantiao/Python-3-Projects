# age calculator

def ageCalc():


    age = int(input("Please type in your age: "))

    print ("You have been alive for " + (age * 365) + "days!")

    print ("You have been alive for " + (age * 365 * 24) + "hours!")

    print ("You have been alive for " + (age * 365 * 24 * 60) + "minutes!")

    print ("You have been alive for " + (age * 365 * 24 * 60 * 60) + "seconds!")

    print ("You have been alive for " + (age * 365 * 24 * 60 * 60 * 1000) + "milliseconds!")

    print ("You have been alive for " + (age * 365 * 24 * 60 * 60 * 1000 * 1000000) + "microseconds!")

    print ("You have been alive for " + (age * 365 * 24 * 60 * 60 * 1000 * 1000000 * 1000000000) + "nanoseconds!")

ageCalc()
