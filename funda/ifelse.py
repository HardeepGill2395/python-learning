print ("Enter any two numbers")
a = int(input())
b = int(input())
print("Enter the choice")
ch = int(input())
print("1. Additon\n")
print("2. Multiplication\n")
print("3. Substraction\n")
print("4. Decimal Division\n")
print("5. integer division\n")
if ch==1:
    print ("addition is " + str(a+b))
elif ch==2:
    print ("multiplication is " + str(a*b))
elif ch==3:
    print ("Substraction is " + str(a-b))
elif ch==4:
    print ("Decimal division is " + str(a/b))
elif ch==5:
    print ("Integer division is " + str(a//b))
else:
    print ("fuck off")
