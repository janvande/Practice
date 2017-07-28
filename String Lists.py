#yourString = input('Please provide a string, we will check if it is a palindrome - Bob')
#listString = []
#revString = []
#stringLength = len(yourString)
#for char in yourString:
#    listString.append(char)
#for revcar in range(stringLength):
#    revString.append(yourString[((stringLength-1)-revcar)])
#test1 = ''.join(listString)
#test2 = ''.join(revString)
#if test1.upper() == test2.upper():
#    print(str(yourString) + ' - is a palindrome')
#else:
##    revName = ''.join(revString)
#   print(revName + ' - is not a palindrome for - ' + revName)



#wrd=input("Please enter a word")
#wrd=str(wrd)
#rvs=wrd[::-1]
#print(rvs)
##if wrd == rvs:
#    print("This word is a palindrome")
#else:
#    print("This word is not a palindrome")

#def reverse(word):
#	x = ''
#	for i in range(len(word)):
#		x += word[len(word)-1-i]
#
#word = input('give me a word:\n')
#x = reverse(word)
#if x == word:#
#	print('This is a Palindrome')
#else:
#	print('This is NOT a Palindrome')
word = input('?')
def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) -1-i]
    return x

x = reverse(word)
print(x)



