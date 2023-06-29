from tkinter import *
from socket import timeout
import tkinter as tk
import time
from trackPerson import EuclideanDistTracker
import warnings
warnings.filterwarnings('ignore')
import tkinter as tk, tkinter.font
import PIL.Image
from pymongo import MongoClient
from sqlalchemy import create_engine
import numpy as np
import datetime as dt
from turtle import bgcolor, color
import csv
from io import StringIO
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import gridfs
from tkinter.font import Font
from tkinter import PhotoImage, Tk
from turtle import bgpic
import pymongo
from matplotlib.animation import FuncAnimation
from pymongo import MongoClient
import os
import cv2
from itertools import combinations, count
from datetime import datetime
from PIL import ImageTk, Image
import pprint

date = dt.datetime.now()

cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
# engine = create_engine("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Users"]
collection_name = db["Username"]
collection_pass = db["Password"]
dbb = cluster["Reports"]
collection_name1 = dbb["Violators"]
collection = db["Users"]

# # db = cluster["camera"]
# # dbb = db["images"]

# db = cluster["Reports"]
# collection_name = db["Violators"]
# def Camera():
#        .file.destroy()
#         import Camera


class Dashboard:
    def __init__(self, file):

        self.file = file
        self.file_width = 1040
        self.file_height = 640
        self.file.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
        self.file.config(background="#B2CBC6")
        self.file.resizable(0,0)

        # self.icon = PhotoImage(file='assets/icons/CC2.png')
        # self.file.iconphoto(True, self.icon)


        #===========HEADER==========
        self.header_icon= Image.open('assets/icons/HEADER TYPE WIDGET.png')
        photo = ImageTk.PhotoImage(self.header_icon)
        self.header = Label(self.file, image=photo, bg="#B2CBC6")
        self.header.image = photo
        self.header.place(x=277, y=0)

        self.time_holder= Image.open('assets/icons/TIME PLACEHOLDER.png')
        photo = ImageTk.PhotoImage(self.time_holder)
        self.time_label= Label(self.file, image=photo, bg="#B2CBC6")
        self.time_label.image = photo
        self.time_label.place(x=700, y=0) 
        # self.header = Frame(self.file, bg='#015C5A')
        # self.header.place(x=277, y=0, width=1070, height=60)
        # self.intro = Label(self.header,
        #     text=f'TODAY is {date:%A, %B %d, %Y}', bg="#015C5A", font=("", 14, "bold"), fg='white')
        # self.intro.place(x=50, y=10)

        # #==========LOGOUT BUTTON ====================
        # self.logout_text = Button(self.file, text='Logout', bg='#FFFFFF', font=("", 13, "bold"), fg='black', cursor='hand2', activebackground='#015C5A')
        # self.logout_text.place(x=950, y=15)

        #=========NAVBAR===============
        self.sidebar = Frame(self.file, bg="#132B2F")
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

        self.changeLabel() #first call it manually

    

        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        #=========CONTENTS =============
        # self.heading = Label(self.file, text='Dashboard', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        # self.heading.place(x=325, y=70)

        self.logo_dash = Image.open('assets/icons/DASHBOARD SELECTED.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=10, y=150)

        # self.dash_text = Label(self.sidebar, text='Dashboard', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        # self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=38, y=250)

        self.cam_text = Button(self.sidebar, text='Camera', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF', fg="#74B3BC")
        self.cam_text.place(x=78, y=255)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_notif.image = photo
        self.logo_notif.place(x=37, y=325)

        self.notif_text = Button(self.sidebar, text='Notification', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.notif_text.place(x=77, y=328)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=38, y=395)

        self.data_text = Button(self.sidebar, text='Database', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.data_text.place(x=38, y=395)


        self.logout = Image.open('assets/icons/logout.png')
        photo = ImageTk.PhotoImage(self.logout)
        self.logout_btn = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logout_btn.image = photo
        self.logout_btn.place(x=38, y=545)

        self.logout_text = Button(self.sidebar, text='Logout', bg='#132B2F', font=("", 18, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.logout_text.place(x=95, y=548)
        #========FOR TABLES==============
        

        self.bodyframe1 = Frame(self.file, bg="#253045")
        self.bodyframe1.place(x=328, y=110, width=640, height=290)

        def plot():
            df = pd.read_csv(r"xlsx_csv.csv")

            x = []
            y = []

            fig, ax = plt.subplots()
            ax.plot(x,y)

            counter = count(0,1)

            def update(i):
                idx=next(counter)
                x.append(df.iloc[idx,0])
                y.append(df.iloc[idx,1])
                plt.cla()
                ax.plot(x,y)

            ani = FuncAnimation(fig=fig,func=update,interval=200)
            # plt.show()

            # plot1 = fig.add_subplot(111)
        
            # plotting the graph
            ax.plot(x,y)
        
            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig,
                                    master = self.bodyframe1)  
            canvas.draw()
        
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()
        
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas,
                                        self.bodyframe1)
            toolbar.update()
        
            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()


        plot_button = Button(master = self.bodyframe1, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot").pack()
       
        #=========REPORTS================'

        # dict_list = list( collection_name.find({"Date": f'{date:%A, %B %d, %Y}'}) )

        # people_list = collection_name.find_one("Number")

        self.bodyframe2 = Frame(self.file, bg="#253045", relief=GROOVE)
        self.bodyframe2.place(x=380, y=435, width=269, height=180)

        shss= collection_name.find_one()
        self.poeple_Report = Label(self.bodyframe2, text='\n'.join([f"{k}: {v}" for k,v in shss.items()]), bg='#253045', font=("", 11, "bold"), fg='Black', anchor="center")
        self.poeple_Report.place(x=13, y=10)

        self.bodyframe3 = Frame(self.file, bg="#253045")
        self.bodyframe3.place(x=708, y=435, width=269, height=180)

    def changeLabel(self): 
            self.time2 = time.strftime('%H:%M:%S')
            self.watch.configure(text=self.time2)
            self.time_label.after(200, self.changeLabel) #it'll call itself continuously

def win():
    global file
    file = Tk()
    file.geometry("800x604")
    file.config(bg="#AF5521")
    Dashboard(file)
    obj1 = Dashboard(file)    
    file.mainloop()

if __name__ == '__main__':
    win()
