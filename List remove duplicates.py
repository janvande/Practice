#numbers = list()
numbers = [1,1,2,2,3,3,]
#numbers = set(numbers)
#numbers = list(numbers)
#print(numbers)

def remdup(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

print(remdup(numbers))

def remdupv1(a):
    return list(set(a))

print(remdupv1(numbers))
