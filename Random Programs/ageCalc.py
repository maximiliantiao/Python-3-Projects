# age calculator for fun

import time

def ageCalc(age):

    time.sleep(1)

    print ("You have been alive for %0d days!\n" % (age * 365))

    time.sleep(1)

    print ("You have been alive for %0d hours!\n" % (age * 365 * 24))

    time.sleep(1)

    print ("You have been alive for %0d minutes!\n" % (age * 365 * 24 * 60))

    time.sleep(1)

    print ("You have been alive for %0d seconds!\n" % (age * 365 * 24 * 60 * 60))

    time.sleep(1)

    print ("You have been alive for %0d milliseconds!\n" % (age * 365 * 24 * 60 * 60 * 1000))

    time.sleep(1)

    print ("You have been alive for %0d microseconds!\n" % (age * 365 * 24 * 60 * 60 * 1000 * 1000000))

    time.sleep(1)

    print ("You have been alive for %0d nanoseconds!\n" % (age * 365 * 24 * 60 * 60 * 1000 * 1000000 * 1000000000))

    time.sleep(1)


age = int(input("Please type in your age: "))
ageCalc(age)
