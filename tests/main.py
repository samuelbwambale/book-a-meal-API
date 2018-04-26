# a function that returns a list of values from 200 to  320 inclusive, 
# list of values divisible by 7 and also divisible by 5


def hello_andela():
    return "Helloworld"

def challange(value):
    return (x for x in range(value))

def myFunction():
    myList = [y for y in range(200,321) if y % 7 == 0 and y % 5 == 0]
    return myList
