from tkinter import *
from PIL import Image, ImageTk
window=Tk()
open_image=Image.open("C:\\Users\\DELL\\Desktop\\guido.jfif")
cimage= ImageTk.PhotoImage(open_image)
L1=Label(window,image=cimage)
#L1.image = cimage
L1.place(x=20, y=20)
window.mainloop()
