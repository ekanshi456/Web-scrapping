import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("URL Shortener")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My url shortener", font="poppins").pack(pady=14)
Entry(root, textvariable=url).pack(pady=8)
Button(root, text="Generate Short url", command=urlshortener).pack(pady=10)
Entry(root, textvariable=url_address).pack(pady=8)
Button(root, text="Copy URL", command = copyurl).pack(pady=8)

root.mainloop()



