# Taking list of elements and then putting in even or odd file respectively
n=int(input("Enter size:"))

even_file=open("even.txt","w")
odd_file=open("odd.txt","w")
l=[]
for i in range(n):
    a= input()
    l.append(a)

for i in l:
    if(int(i)%2==0):
        even_file.write(i)
    else:
        odd_file.write(i)

even_file=open("even.txt","r")
odd_file=open("odd.txt","r")
e=even_file.read()
print(e)

even_file.close()
odd_file.close()




