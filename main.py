import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

#from tkinter import *
window = tk.Tk()

window.title("Sketching")
window.geometry('1200x800')

#header
header = tk.Label(window, text="GET YOUR IMAGE SKETCHED HERE!", bg="red", fg="black" ,font=("none bold",35), anchor="n") 
#anchor=n for top-central justification
header.place(x=300,y=1)
#header.pack()

#left frame
left_frame = tk.Frame(window, width=400, height=400, highlightbackground="black", highlightthickness=1)
left_frame.place(x=40,y=150)
left_frame.pack_propagate(0)

#left image label
# inp_image = tk.Label(left_frame, text="Input Image", font=("none Bold",10))
# inp_image.pack()


#left label
left_label = tk.Label(window, text="Input Image", font=("none Bold",20))
left_label.place(x=200,y=120)


#rigt_frame
rigt_frame = tk.Frame(window, width=400, height=400, highlightbackground="black", highlightthickness=1)
rigt_frame.place(x=760,y=150)
rigt_frame.pack_propagate(0)

#right image label
# out_image = tk.Label(rigt_frame, text="Output Image", font=("none Bold",10))
# out_image.pack()



#right label
right_label = tk.Label(window, text="Output Image", font=("none Bold",20))
right_label.place(x=930,y=120)



class variables:
    img = ""
    inp_img = ""
    out_img = ""

    #left image label
    inp_image = tk.Label(left_frame, text="Input Image", font=("none Bold",10))
    inp_image.pack()

    #right image label
    out_image = tk.Label(rigt_frame, text="Output Image", font=("none Bold",10))
    out_image.pack()

def working_design():
    #image selection button
    img_selection_btn = tk.Button(window, text="Select Image", fg="black", font=("none Bold",20) , command=open_file)
    img_selection_btn.place(x=520, y=100)
    #*--------------------------------
    # #sketching button
    img_sketching_btn = tk.Button(window, text="Sketch", fg="black", font=("none Bold",20) , command=Sketching)
    img_sketching_btn.place(x=520, y=150)


def open_file(): 
    filename = filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),("PNG","*.png"),("All Files","*.*"))) 

    if filename!="" :
        variables.img = cv2.imread(filename)
        #resizing for image display
        variables.inp_img = resize_img(variables.img)
        #Rearranging the color channel
        b,g,r = cv2.split(variables.inp_img)
        img = cv2.merge((r,g,b))

        #convert image object into TkPhoto object
        im = Image.fromarray(img)
        img1 = ImageTk.PhotoImage(image=im)

        variables.inp_image.pack_forget()
        left_frame.update()

        variables.inp_image = tk.Label(left_frame, image=img1)
        variables.inp_image.image = img1
        variables.inp_image.pack()
        left_frame.update()

        
        
 

def resize_img(img):
    
    img1 = cv2.resize(img,(400,400)) #(a high-quality downsampling filter)       
    return img1

def Sketching():
    img_rgb = variables.img
    print("inp img:",img_rgb.shape)

    #convert to gray scale
    grayImage = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    #invert the gray image
    grayImageInv = 255 - grayImage

    #Apply gaussian blur
    grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)

    #blend using color dodge
    img = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)
    
    #resizing for image display
    variables.out_img = resize_img(img)
    
    #convert image object into TkPhoto object
    im = Image.fromarray(variables.out_img)
    img1 = ImageTk.PhotoImage(image=im)
    
    variables.out_image.pack_forget()
    rigt_frame.update()

    variables.out_image = tk.Label(rigt_frame, image=img1)
    variables.out_image.image = img1
    variables.out_image.pack()
    rigt_frame.update()


working_design()

window.mainloop()

'''
import cv2
import sys

#read image
image = cv2.imread("../assets/anish.jpg")

#check if image exists
if image is None:
    print("can not find image")
    sys.exit()

#convert to gray scale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#invert the gray image
grayImageInv = 255 - grayImage

#Apply gaussian blur
grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)

#blend using color dodge
output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)

#create windows to dsiplay images
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)

#display images
cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)

#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()'''
