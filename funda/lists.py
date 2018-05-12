a = []
print("Enter 10 numbers : \n")
for i in range (10):
    n = int(input())*12.5
    a.append(n)
#without using range
for elem in a:
    print (elem,end=',')

#with using range

for i in range (len(a)):
                print(a[i])
