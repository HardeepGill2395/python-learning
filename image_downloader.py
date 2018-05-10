import requests
import pyperclip
url = pyperclip.paste()
r = requests.get(url)
with open ("raazi.mp3","wb") as f:
    for chunks in r.iter_content(10000):
        f.write(chunks)

print("file downloaded")
