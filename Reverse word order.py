sentence = input('Please provide a few words?')


def function(sentence):
    makelist = sentence.split()
    reverse = []

    for i in range(len(makelist)):
        reverse.append(makelist[-1 - int(i)])
    reverse = ' '.join(reverse)
    return reverse


print(function(sentence))
