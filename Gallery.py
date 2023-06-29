from tkinter import *
from socket import timeout
import tkinter as tk
import time
from trackPerson import EuclideanDistTracker
import warnings
warnings.filterwarnings('ignore')
import tkinter as tk, tkinter.font
import scipy as sp
import PIL.Image
from pymongo import MongoClient
from sqlalchemy import create_engine
import numpy as np
import datetime as dt
from turtle import bgcolor, color
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import gridfs
import scipy.linalg
from tkinter.font import Font
import scipy.misc
from tkinter import PhotoImage, Tk, ttk
from turtle import bgpic
import pymongo
from pymongo import MongoClient
import os
import cv2
from itertools import combinations
from datetime import datetime
from PIL import ImageTk, Image
import pprint

date = dt.datetime.now()

# cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
# # engine = create_engine("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
# db = cluster["Users"]
# collection_name = db["Violators"]
# collection = db["Users"]

# # db = cluster["camera"]
# # dbb = db["images"]

# db = cluster["Reports"]
# collection_name = db["Violators"]
# # def Camera():Gall
#        .file.destroy()
#         import Camera


class Gall:
    def __init__(self, pish):

        self.pish = pish
        self.pish_width = 1040
        self.pish_height = 640
        self.pish.geometry(f'{self.pish_width}x{self.pish_height}+{100}+{30}')
        self.pish.config(background="#B2CBC6")
        self.pish.resizable(0,0)

        # self.icon = PhotoImage(pish='assets/icons/CC2.png')
        # self.pish.iconphoto(True, self.icon)


        #===========HEADER==========
        self.header_icon= Image.open('assets/icons/HEADER TYPE WIDGET.png')
        photo = ImageTk.PhotoImage(self.header_icon)
        self.header = Label(self.pish, image=photo, bg="#B2CBC6")
        self.header.image = photo
        self.header.place(x=277, y=0)

        self.time_holder= Image.open('assets/icons/TIME PLACEHOLDER.png')
        photo = ImageTk.PhotoImage(self.time_holder)
        self.time_label= Label(self.pish, image=photo, bg="#B2CBC6")
        self.time_label.image = photo
        self.time_label.place(x=700, y=0) 


        #=========NAVBAR===============
        self.sidebar = Frame(self.pish, bg="#132B2F")
        self.sidebar.place(x=0, y=0, width=275, height=750)

        #=======NAVBAR LOGO===========
        self.logo = Image.open('assets/icons/TEXT.png')
        photo = ImageTk.PhotoImage(self.logo)
        self.logo = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo.image = photo
        self.logo.place(x=10, y=50)

        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        # # self.mFrame = Frame(self.sidebar, bg="#ACFFEA")
        # self.mFrame.place(x=0, y=530, width=280, height=300)

        self.intro = Label(self.time_label,
            text=f'TODAY is \n{date:%A,} \n {date:%B %d, %Y}', bg="#183D3F", font=("", 10, "bold"), fg='#74B3BC')
        self.intro.place(x=10, y=10)
        self.watch = Label(self.time_label, text=self.time2, font=('times',18,'bold'), fg='#74B3BC', bg="#183D3F")
        self.watch.place(x=160, y=20)

        #==========LOGOUT BUTTON ====================
        self.logout = Image.open('assets/icons/logout.png')
        photo = ImageTk.PhotoImage(self.logout)
        self.logout_btn = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logout_btn.image = photo
        self.logout_btn.place(x=38, y=545)

        self.logout_text = Button(self.sidebar, text='Logout', bg='#132B2F', font=("", 18, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.logout_text.place(x=95, y=548)
        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        #=========CONTENTS =============

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=38, y=150)

        self.dash_text = Label(self.sidebar, text='Dashboard', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F")
        self.dash_text.place(x=80, y=158)

        self.dash_text = Button(self.sidebar, text='Dashboard', 
           bg="#132B2F", font=("", 13, "bold"), 
            bd=0, cursor='hand2', activebackground="#132B2F"
            )

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo,bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=38, y=230)

        self.cam_text = Button(self.sidebar, text='Camera', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F")
        self.cam_text.place(x=78, y=235)

        self.logo_dash = Image.open('assets/icons/GALLERY SELECTED.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=10, y=300)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=38, y=395)

        self.data_text = Button(self.sidebar, text='Database', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F")
        self.data_text.place(x=78, y=395)



        #========FOR TABLES==============
        self.bodyframe1 = Frame(self.pish, bg="#253045")
        self.bodyframe1.place(x=280, y=100, width=750, height=520)

        self.bodycanvas = Canvas(self.bodyframe1)
        self.bodycanvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.bodyscroll = ttk.Scrollbar(self.bodyframe1, orient=VERTICAL, command=self.bodycanvas.yview)
        self.bodyscroll.place(relx=1, rely=0, relheight=1, anchor='ne')

        self.bodyscroll2 = ttk.Scrollbar(self.bodyframe1, orient=HORIZONTAL, command=self.bodycanvas.xview)
        self.bodyscroll2.place(relx=0, rely=0, relwidth=1, anchor='nw')

        self.bodycanvas.configure(yscrollcommand=self.bodyscroll.set)
        self.bodycanvas.configure(xscrollcommand=self.bodyscroll2.set)

        self.bodycanvas.bind('<Configure>', lambda e: self.bodycanvas.configure(scrollregion=self.bodycanvas.bbox("all")))

        self.seccanvs = Frame(self.bodycanvas)

        self.bodycanvas.create_window((0,0), window=self.seccanvs, anchor='nw')

        files = []
        path = 'C:/Users/Client/OneDrive/Documents/Python projects/New folder/Capture'

        for file in os.listdir(path):
            if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
                files.append(file)
                print(file)
        
        MAX_ROWS = 4
        current_row = 0

        i = 0
        
        def view_image(event=None):
            
            

            print("image clicked")

        while i <= (len(files))-1:

            dirImg = path + '/' + files[i]
            loading = Image.open(dirImg)
            loading.thumbnail((120,120))
            renderiza = ImageTk.PhotoImage(loading)            
            
            i = i + 1

            imagemA = Button(self.seccanvs, image=renderiza, command=view_image)
            imagemA.image = renderiza
            
            imagemA.grid(column=i, row=current_row, columnspan=5,ipadx=5, ipady=5, sticky=NSEW)
            current_row += 1
            if (current_row >= 4):
                i += 1
                current_row = 0

            




def win():
    global pish
    pish = Tk()
    pish.geometry("800x604")
    pish.config(bg="#071D20")
    Gall(pish)    
    pish.mainloop()

if __name__ == '__main__':
    win()

# from tkinter import *
# from PIL import Image, ImageTk

# import os

# class ImageViewer:

#     def __init__(self, root):
        
#         self.root = root
#         self.root.title("Photo Viewer")
#         self.root.geometry("1360x750")
#         self.root.config(bg = "lightblue")

#         menus = Menu(self.root)
#         self.root.config(menu = menus)

#         file_menu = Menu(menus)
#         menus.add_cascade(label = "File", menu = file_menu)
        
#         file_menu.add_command(label = "Open", command = self.open_dialog)
#         file_menu.add_separator()
#         file_menu.add_command(label = "Previous", command = self.previous_img)
#         file_menu.add_command(label = "Next", command = self.next_img)
#         file_menu.add_separator()
#         file_menu.add_command(label = "Exit", command = self.root.destroy)

#         self.label = Label(self.root, text = "Open a image using open menu", font = ("Helvetica", 15), foreground = "#0000FF", background = "lightblue")
#         self.label.grid(row = 0, column = 0, columnspan = 4)

#         self.buttons()

#     def path_func(self, path):
#         l = []
#         self.path = path.split('/')
#         self.path.pop()

#         self.path = '/'.join([str(x) for x in self.path])
        
#         #print(self.path)
        
#         for file in os.listdir(self.path):
#             if file.endswith('.jpg') or file.endswith('.png'):
#                 l.append(file)
#                 #print(l)

#         def join(file):
#             os.chdir(self.path)
#             #print(os.getcwd())
#             cwd = os.getcwd().replace('\\', '/')
#             #print(cwd)
#             f = cwd + '/' + file
#             #print(f)
#             return f
        
#         global file_list
#         file_list = list(map(join, l))
#         #print(file_list) 

#     def open_dialog(self):
#             global file_name
#             file_name = filedialog.askopenfilename(initialdir = "C:/Users/Client/OneDrive/Documents/Python projects/CountMe - main/images", title = "Open file")
#             #print(file_name)
#             self.view_image(file_name)
#             self.path_func(file_name)

#             '''except:
#             label = Label(self.root, text = "Select a file to open")
#             label.grid(row = 4, column =1)'''

#     def view_image(self, filename):
#         try:
#             self.label.destroy()
#             global img
#             img = Image.open(filename)
#             img = img.resize((500, 450))
#             img = ImageTk.PhotoImage(img)
        
#         #print(img)

#             show_pic = Label(self.root, image = img)
#             show_pic.grid(row = 1, column = 0, columnspan = 3)

#         except:
#             pass
        
#     def buttons(self):
#         open_button = Button(self.root, text = "Browse", command = self.open_dialog, background = "lightblue")
#         open_button.grid(row = 1, column = 1)
        
#         previous_button = Button(self.root, text = "Previous", command = self.previous_img, background = "lightblue", width = 25)
#         previous_button.grid(row = 3, column = 0, pady = 10)

#         empty = Label(self.root, text = "        ", background = "lightblue")
#         empty.grid(row = 3, column = 1)
        
#         next_button = Button(self.root, text = "Next", command = self.next_img, background = "lightblue", width = 25)
#         next_button.grid(row = 3, column = 2)


#     def previous_img(self):
#         global file_name
#         #print(file_list)
#         index = file_list.index(file_name)
#         #print(index)
#         curr = file_list[index - 1]
#         #print(curr)
#         self.view_image(curr)
#         file_name = curr


#     def next_img(self):
#         global file_name
#         index = file_list.index(file_name)
#         #print(index)
#         if index == len(file_list) - 1:
#             index = -1
#             curr = file_list[index + 1]
#             #print(curr)
#             self.view_image(curr)
#             file_name = curr
#         else:
#             curr = file_list[index + 1]
#             #print(curr)
#             self.view_image(curr)
#             file_name = curr

# if __name__ == "__main__":
#     root = Tk()
#     gallery = ImageViewer(root)
#     root.mainloop()