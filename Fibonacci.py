
howMany = 0



def fibornacci(howMany):
    a = 0
    b = 1
    sequence=[1]
    for i in range(1, int(howMany)):
        c = a + b
        a = b
        b = c
        sequence.append(c)
    return sequence

howMany = input('How many fubornacci number do you want to see?')
print(fibornacci(howMany))
