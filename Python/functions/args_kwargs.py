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
    result2=""
    for x in kwargs.values():    #we take .values() beacause iterable object(kwargs) is a dictionary
        result += x

    for y in kwargs:
        result2 +=y

    return result, result2

print(concatenate(a="Hello", b="World"))



my_list=[1,2,3]
print(my_list)
print(*my_list)

#the unpacking operator is also used to pack things:-

list2=[1,2,3,4,5,6,7,8]
a,*b,c=list2

print (a)
print (b)
print (c)


d=[*"HelloWorld"]
print(d)


#came in Pyhton in Python2.5