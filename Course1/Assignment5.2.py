#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largestNumber = -1
smallestNumber = None
while True :
    enterInput = input('Enter a Number: ')
    try :
        number = int(enterInput)
        if number > largestNumber :
            largestNumber = number
        if smallestNumber is None :
            smallestNumber = number
        if number < smallestNumber:
            smallestNumber = number
    except :
        if enterInput == 'done' :
            break
        print('Invalid input') 
        continue 
print('Maximum is', largestNumber)
print('Minimum is', smallestNumber)  

