from moviepy.editor import VideoFileClip
import pygame

pygame.display.set_caption('My video!')

clip = VideoFileClip('GIF_loup_raté.mp4')
clip.preview()
pygame.quit()

# # from PIL import Image,ImageTk
# from tkinter import *


# from tkinter import *
# import time
 
# fen = Tk()
 
# can = Canvas(fen, width=350, height=200, bg='white')
# can.pack(side='top', fill='both', expand='yes')
# photo = PhotoImage(file="img/wolf_short.gif")
# can.create_image(0,0,anchor='nw', image=photo, tag='photo')
 
# ind = -1
# def update(delay=200):
#     global ind
#     ind += 1
#     if ind == 8: ind = 0
#     print (ind)
#     photo.configure(format="gif -index " + str(ind))
#     fen.after(delay, update)
 
# update()
# fen.mainloop()

# import tkinter as tk 

# def add_image(): 
#     text.image_create(tk.END, image = img) # Example 1 
#     text.window_create(tk.END, window = tk.Label(text, image = img)) # Example 2 

# root = tk.Tk() 

# text = tk.Text(root) 
# text.pack(padx = 20, pady = 20) 

# tk.Button(root, text = "Insert", command = add_image).pack() 

# img = tk.PhotoImage(file = "img/wolf.GIF") 

# root.mainloop() 

#img = PhotoImage(file = "img/wolf.GIF") 
# img/wolf_short.gif
