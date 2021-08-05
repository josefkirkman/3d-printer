import sys
import tkinter
import PIL
import time
from PIL import Image, ImageTk
print(sys.argv)
bbrash = Image.open (sys.argv[1])

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    root.wm_attributes('-fullscreen','true')
    
    root.geometry("%dx%d+0+0" % (w, h))
    #root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    

    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()


showPIL(bbrash)

