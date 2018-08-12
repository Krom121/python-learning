# funtions

# create a function

def sayHello(name = 'stephen'):
    print('hello', name)
sayHello('john')

# return a value

def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1, 2)
print(numSum)

def addOneToNum(num):
    num = num + 1
    print('value inside function:', num)
    return

num = 5
addOneToNum(num)
print('value outside function:', num)

def addOneToList(myList):
    myList.append(4)
    print('value inside function:', myList)
    return

myList = [1, 2, 3]
addOneToList(myList)
print('value outside function:', myList)