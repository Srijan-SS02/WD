def sum(*args):
    result = 0
    for x in args:
        result += x
        
    return result 

print(sum(1,2,3))

def sum2(*args):
    result = 0
    for x in args:
        result += x
        
    return result 

l=[1,2,3]
print(sum2(*l)) # '*' Operator is unpacking operator



def concatenate(**kwargs):
    result =""
    for x in kwargs.values():
        result += x

    return result

print(concatenate(a="Hello", b="World"))