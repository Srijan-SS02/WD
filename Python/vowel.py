s=input("Enter any string")

for i in s:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        continue
    else:
        print(i, end="") 