yourString = input('Please provide a string, we will check if it is a palindrome - Bob')
listString = []
revString = []
stringLength = len(yourString)
for char in yourString:
    listString.append(char)
for revcar in range(stringLength):
    revString.append(yourString[((stringLength-1)-revcar)])
test1 = ''.join(listString)
test2 = ''.join(revString)
if test1.upper() == test2.upper():
    print(str(yourString) + ' - is a palindrome')
else:
    revName = ''.join(revString)
    print(revName + ' - is not a palindrome for - ' + revName)


