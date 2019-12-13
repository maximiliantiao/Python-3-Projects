# variable
binaryPrompt = "\nThe binary representation is: "
error = "Error: Invalid program argument"
resultA = 0
resultB = ""
finalResult = ""
numberOfC = 0
numberOfL = 0
numberOfX = 0
numberOfV = 0
numberOfI = 0

# Prompt
prompt = raw_input("You entered the Roman numural: \n")



# Iterate through numeral input and assign specific value to specific characters
# based on specific characters (e.g. X = 10). Also check the input for valid characters (e.g. M is not
# a valid character) and check for valid number of certain characters

numArr = []
for x in range(len(prompt)):
    numA = prompt[x]
    # Assign values to array with current character
    if numA == "C":
        numArr.append(100)
        numberOfC += 1
    elif numA == "L":
        numArr.append(50)
        numberOfL += 1
    elif numA == "X":
        numArr.append(10)
        numberOfX += 1
    elif numA == "V":
        numArr.append(5)
        numberOfV += 1
    elif numA == "I":
        numArr.append(1)
        numberOfI += 1
    else:
        print(error)
        exit()

# Checking for invalid use of numerals
if numberOfI >= 4:
    print(error)
    exit()
elif numberOfV > 1:
    print(error)
    exit()
elif numberOfL > 1:
    print(error)
    exit()
else:
    pass

# Convert to numerals to integer
numArr.append(0)
#print (numArr)

# Combine array that have subtractive pairs
x = 0
y = 1
numArr2 = [];
while x <= len(numArr)-1 and y <= len(numArr)-1:
    if numArr[x] < numArr[y]:
        if numArr[x] == 1 and numArr[y] == 5:
            numArr2.append(numArr[y] - numArr[x])
            x += 2
            y += 2
        elif numArr[x] == 1 and numArr[y] == 10:
            numArr2.append(numArr[y] - numArr[x])
            x += 2
            y += 2
        elif numArr[x] == 10 and numArr[y] == 50:
            numArr2.append(numArr[y] - numArr[x])
            x += 2
            y += 2
        elif numArr[x] == 10 and numArr[y] == 100:
            numArr2.append(numArr[y] - numArr[x])
            x += 2
            y += 2
    
        else:
            print(error)
            exit()
    else:
        numArr2.append(numArr[x])
        x += 1
        y += 1

numArr2.append(0)
#print(numArr2)

# Combine array and check for invalid inputs, return integer to resultA
#if len(numArr2) >= 3:
x = 0
y = 1
while x <= len(numArr2)-1 and y <= len(numArr2)-1:
    if numArr2[x] >= numArr2[y]:
        resultA += numArr2[x]
        x += 1
        y += 1
    else:
        print(error)
        exit()
#elif len(numArr2) <= 2:
#    resultA = numArr2[0]
#    print(resultA)
#else:
#    print(error)
#    exit()

print(resultA)

# Integer to binary, return binary to resultB

if (resultA - 256) >= 0:
    resultA -= 256
    resultB += "1"
else:
    resultB += "0"

if resultA >= 128:
    resultA -= 128
    resultB += "1"
else:
    resultB += "0"

if resultA >= 64:
    resultA -= 64
    resultB += "1"
else:
    resultB += "0"

if resultA >= 32:
    resultA -= 32
    resultB += "1"
else:
    resultB += "0"

if resultA >= 16:
    resultA -= 16
    resultB += "1"
else:
    resultB += "0"

if resultA >= 8:
    resultA -= 8
    resultB += "1"
else:
    resultB += "0"

if resultA >= 4:
    resultA -= 4
    resultB += "1"
else:
    resultB += "0"

if resultA >= 2:
    resultA -= 2
    resultB += "1"
else:
    resultB += "0"

if resultA >= 1:
    resultA -= 1
    resultB += "1"
else:
    resultB += "0"


for x in range(len(resultB)-1):
    if resultB[x] == "1":
        while x <= len((resultB))-1:
            finalResult += resultB[x]
            x += 1
        
        break
    else:
        pass




print(binaryPrompt)
print("Ob" + finalResult + "\n")
exit()
