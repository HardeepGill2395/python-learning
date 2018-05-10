import pyperclip
import webbrowser
import requests

choice = 0
fname = ""
ext = ""
d = {1:"jpg" , 2:"txt" , 3:"mp3"}

def takeinput():
    url = input("Enter the url\n")
    print("enter the choice \n1.image \n2.text \n3.video")
    ch = int(input())
    fname = input("enter file name")
    s = fname + "." + d[ch]
    return [s,url,ch]

def fetchdata(url):
    r = requests.get(url)
    return r


def savedata(r,fname,ch):
    if ch == 2:
        with open(fname,"w") as f:
            f.write(r.text)
    elif ch==1 or ch==3:
        with open(fname,"wb") as f:        
            for chunks in r.iter_content(10000):
                f.write(chunks)
    print("file Saved")

fname,url,ch = takeinput()
r = fetchdata(url)
savedata(r,fname,ch)
