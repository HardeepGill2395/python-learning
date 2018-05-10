'''
f = open("sail.txt","r")
print (f.read())
f.close()
'''
#read file
with open("sail.txt","r") as f:
    print (f.read())

#Write file
with open("hardeep.txt","w") as f:
    f.write("Hello \n I am Hardeep")

g = open("yo.txt","w")
g.write ("hey \nwassup man??")
g.close()
