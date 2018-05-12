a = []
for i in range (3):
    print("Enter the name of the movie\n")
    name = input()
    print("Enter the rating of the movie\n")
    rate = float(input())
    print("Enter the review of the movie\n")
    rev = input()
    d = {"Name":name,"Rating":rate,"Review":rev}
    a.append(d)

for i in a:
    print ("Name of the movie is " + i["Name"])
    print ("Rating of the movie is" + str(i["Rating"]))
    print ("Review of the movie is" + i["Review"])
