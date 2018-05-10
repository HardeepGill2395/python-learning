import pyperclip
import webbrowser
import requests

url = 0
choice = 0
fname = " "
ext = " "
d = {"1.":"image" , "2.":"text" , "3.":"video"}

def takeinput ():
    url = input ("Enter the url\n")
    print("enter the choice \n1.image \n2.text \n3.video")
    ch = int(input)
    fname = input("enter file name")
    s = fname + "." + d(ch)
    return (s)

def fetchdata (url):
    
    r = requests.get(url)


def savedata(r,fname):
    with open ("s","wb") as f:
    for chunks in r.iter_content(10000):
        f.write(chunks)
    print ("file Saved")
