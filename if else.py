n = int(input())
x = n>100
y = n%10 == 0
print(x)
if x and y:
    if x ==200:
        print("200")
    else:
        print("Not 200")
    print("Greater")
elif n<30 :
    print("less")
else:
    print("nope")
