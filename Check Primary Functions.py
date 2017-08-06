#print('This code will print all the divisors to a random input number you provide.\n')
newNum = input('Please provide any number; we will calculate the divisors')
diVisors = []
testDiv = range(2, int(newNum))
for elem in testDiv:
    if int(newNum) % elem == 0:
        diVisors.append(elem)
        print(str(elem) + ' Is a divisor of ' + newNum)
print('These are all the divisors - ' + str(diVisors))


