from tkinter import *
from socket import timeout
import tkinter as tk
from tkinter import messagebox
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
from io import StringIO
import pandas
import matplotlib.pyplot as plt
import gridfs
from tkinter.font import Font
from tkinter import PhotoImage, Tk
from turtle import bgpic
import pymongo
from pymongo import MongoClient
import os
import cv2
from itertools import combinations
from datetime import datetime
from PIL import ImageTk, Image

date = dt.datetime.now()

try:
    cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
    cluster.server_info()
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)

db = cluster["Reports"]
collection_name = db["Violators"]

class Database:
    def __init__(self, records):

        self.records = records
        self.file_width = 1040
        self.file_height = 640
        records.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
        self.records.config(background="#B2CBC6")
        self.records.resizable(0,0)

        self.icon = PhotoImage(file='assets/icons/CC2.png')
        self.records.iconphoto(True, self.icon)

        

        #===========HEADER==========
        

        #==========LOGOUT BUTTON ====================

        #=========NAVBAR===============
        self.sidebar = Frame(self.records, bg="#132B2F")
        self.sidebar.place(x=0, y=0, width=275, height=750)

        #=======NAVBAR LOGO===========
        self.logo = Image.open('assets/icons/TEXT.png')
        photo = ImageTk.PhotoImage(self.logo)
        self.logo = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo.image = photo
        self.logo.place(x=10, y=50)

        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        #=========CONTENTS =============

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=35, y=255)

        self.dash_text = Label(self.sidebar, text='Dashboard', bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', bd=0, cursor='hand2', activebackground='#132B2F')
        self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=35, y=310)

        self.cam_text = Button(self.sidebar, text='Camera', bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', bd=0, cursor='hand2', activebackground='#132B2F')
        self.cam_text.place(x=75, y=315)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_notif.image = photo
        self.logo_notif.place(x=35, y=365)

        self.notif_text = Button(self.sidebar, text='Notification', bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', bd=0, cursor='hand2', activebackground='#132B2F')
        self.notif_text.place(x=75, y=368)

        self.logo_dash = Image.open('assets/icons/DATABASE SELECTED.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=10, y=415)

        self.logout = Image.open('assets/icons/logout.png')
        photo = ImageTk.PhotoImage(self.logout)
        self.logout_btn = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logout_btn.image = photo
        self.logout_btn.place(x=38, y=545)

        self.logout_text = Button(self.sidebar, text='Logout', bg='#132B2F', font=("", 18, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.logout_text.place(x=95, y=548)

        #========FOR TABLES==============
        self.bodyframe1 = Frame(self.records, bg="#FFFFFF")
        
        self.bodyframe1.place(x=328, y=110, width=1040, height=590)

        # self.table2 = Frame(self.records, bg="#FFFFFF")
        # self.table2.place(x=625, y=70, width=840, height=40)
        
        serts = StringVar()

        def sertz():
            
            datee = self.search.get()

            dict_list = list( collection_name.find({"Date": datee}) )
            
            # dict_list[0:2]
            # [   {    u'Name': u'People', 
            #     }, 
            #     {    u'Name': u'People', 
            #     }
            # ]
            
            for doc in dict_list[:5]:

                lisi = dict_list.append(doc)
                # dict_list.append(doc)
                tablelabel = Label(self.bodyframe1, text='\n\n         '.join([f"{k}: {v}" for k,v in doc.items()]),
                 width=100, height=10, bg="#FFFFFF", anchor='w', justify='left',relief=GROOVE)
                tablelabel.config(font=("Courier", 7), fg='black')
                tablelabel.grid(column=3, row=lisi, sticky=SW, rowspan=2, columnspan=5,padx=10, pady=3)
                # rasi.append(tablelabel)

            scroll = Scrollbar(self.bodyframe1, orient='vertical', command=doc)
            scroll.grid(row=0, column=1, sticky='ns')
            dict_list['yscrollcommand'] = scroll.set

        self.search = Image.open('assets/icons/DATABASE WIDGET.png')
        photo = ImageTk.PhotoImage(self.search)
        self.search_label= Label(self.records, image=photo, bg='#B2CBC6')
        self.search_label.image = photo
        self.search_label.place(x=305, y=0)
        
        def click(*args):
            self.search.delete(0, 'end')
        # def leave(*args):
        #     # self.search.delete(0, 'end')
        #     self.search.insert(0, '(Date. ex. Friday, then (M/D/Y)')
        #     # self.records.focus()

        self.search = Entry(self.search_label, textvariable = serts, bg="#FFFFFF",width=30)
        self.search.insert(0, '(Date. ex. Friday, then (M/D/Y)')
        self.search.place(x=190, y=30)
        self.search.bind("<Button-1>", click)
        # self.search.bind("<Leave>", leave)
        self.sertsbtn = Button(self.search_label, text = "Search", width = 10, height = 1, command = sertz).place(x=400, y=25)

def win():
    global records
    records = Tk()
    records.geometry("800x604")
    records.config(bg="#071D20")
    Database(records)    
    records.mainloop()

if __name__ == '__main__':
    win()
