print("Enter the name of the movie\n")
name = input()
print("Enter the rating of the movie\n")
rate = float(input())
print("Enter the review of the movie\n")
rev = input()

d = {"Name":name,"Rating":rate,"Review":rev}
print ("Name of the movie is " + name)
print ("Rating of the movie is" + str(rate))
print ("Review of the movie is" + rev)
for i in d.keys():
    print("Keys are: " + i)
for i in d.values():
    print("Values are: " + str(i))
