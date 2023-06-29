#  TABLE OF CONTENTS, JUST FIND TO LOCATE CODE PARTS
# 
# DEPENDENCIES, DATABASE AND CV CONNECTIONS, NAVIGATIONS, LOGIN USER, REGISTER USER, LOGINPAGE FORM, DASHBOARD, CAMIIRA, DATABASE
# 
#  

#---------------------------DEPENDENCIES IMPORT------------

#--------------GUI
import tkinter as tk, tkinter.font
from tkinter import *
import tkinter as tk
import PIL.Image
from turtle import bgcolor, color
from tkinter.font import Font
from tkinter import PhotoImage, Tk, ttk
from turtle import bgpic
from PIL import ImageTk, Image
from matplotlib.animation import FuncAnimation
#---------------DATABASE
from pymongo import MongoClient
from sqlalchemy import create_engine
import pandas
import matplotlib.pyplot as plt
import gridfs
import pymongo
from pymongo import MongoClient
import pandas as pd
from itertools import combinations, count
#-------------OPENCV
import cv2
from trackPerson import EuclideanDistTracker
#---------OTHERS
import time
import subprocess
from win10toast import ToastNotifier
import sys
import warnings
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
warnings.filterwarnings('ignore')
from socket import timeout
import numpy as np
import datetime as dt
from io import StringIO
import os
from itertools import combinations
from datetime import datetime

#------------DATABASE AND CV CONNECTION --------------------

date = dt.datetime.now()

cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
# engine = create_engine("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Users"]
collection_name = db["Username"]
collection_pass = db["Password"]
dbb = cluster["Reports"]
collection_name1 = dbb["Violators"]

tracker = EuclideanDistTracker()
# wht = 400
confThreshold = 0.3
nmsThreshold = 0.3

collection = db["Users"]
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fs = gridfs.GridFS(db)
file = "C:/Users/Client/OneDrive/Documents/Python projects/New folder/Capture/"

classesFile = 'coco.names'
className = []
with open(classesFile, 'rt') as f:
    className = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')  
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)    
classes = []
with open('coco.names','r') as f:
    classes =f.read().splitlines()
print(classes)
cap = cv2.VideoCapture(0)
output_layers = net.getUnconnectedOutLayersNames()
print(output_layers)

# fs = gridfs.GridFS(db)
# gridfs.GridFS.find_one
# dash = fs.get({'filename': "dash"})
# fs.get(dash).read()

#-----------------------------NAVIGATION-----------

def delete2():
      screen3.destroy()

def delete3():
      screen4.destroy()

def delete4():
      screen5.destroy()

def datapage():
    cammish.withdraw()
    global records
    records = tk.Toplevel()
    Database(records)
    records.mainloop()
# def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

def nextpage():
    window.withdraw()
    screen3.destroy()
    global dash
    dash = tk.Toplevel()
    dash.geometry("800x604")
    dash.config(bg="#071D20")
    Dashboard(dash)
    dash.mainloop()


def campage():
    dash.withdraw()
    global cammish
    cammish = tk.Toplevel()
    Camiira(cammish)
    cammish.mainloop()

def gallpage():
    dash.withdraw()
    global pish
    pish = tk.Toplevel()
    Gall(pish)
    pish.mainloop()

def recordpage():
    dash.withdraw()
    global records
    records = tk.Toplevel()
    Database(records)
    records.mainloop()


def backtodash():
    dash.deiconify()
    cammish.withdraw() or records.withdraw() or pish.withdraw()

def backtocam():
    cammish.deiconify()
    dash.withdraw() or records.withdraw() or pish.withdraw()

def backtogall():
    pish.deiconify()
    dash.withdraw() or cammish.withdraw() or records.withdraw()

def backtodata():
    records.deiconify()
    dash.withdraw() or cammish.withdraw() or pish.withdraw()

#----------------LOGIN AND REGISTER -------------------------





def login_sucess():
    global screen3
    screen3 = Toplevel(window)

    login_bttn = Image.open('assets/placeholder/menu.png')
    photo = ImageTk.PhotoImage(login_bttn)
    login_put= Label(screen3, image=photo, bg='white')
    login_put.image = photo
    login_put.pack()
    entry_button = Button(login_put, font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', text = "OK", command=nextpage)
    entry_button.pack()

    # Label(screen3, text = "Login Sucess").pack()
    # Button(screen3, text = "OK", command=nextpage).pack()
    
def password_not_recognised():
      global screen4
      screen4 = Toplevel(window)
      screen4.title("Success")
      screen4.geometry("150x100")
      Label(screen4, text = "Password Error").pack()
      Button(screen4, text = "OK", command=delete3).pack()

def user_not_found():
      global screen5
      screen5 = Toplevel(window)
      screen5.title("Success")
      screen5.geometry("150x100")
      Label(screen5, text = "User Not Found").pack()
      Button(screen5, text = "OK", command =delete4).pack()      

def login_verify():
            global username1
            username1 = username_verify.get()
            password1 = password_verify.get()
            username_entry1.delete(0, END)
            password_entry1.delete(0, END)
            forname = {"username": username1}
            forpass = {"password": password1}
            result1 = collection.find_one({"username":forname, "password":forpass})

            if result1:

              if result1:
                True
                login_sucess()
                
              else:
                password_not_recognised()

            else:
                user_not_found()
                    
def register_user():

    # for x in results:
    #   print(results["name"])
    username_info = username.get()
    password_info = password.get()

    forname = {"username": username_info}
    forpass = {"password": password_info}
    # collection_name.insert_one(forname)
    # collection_pass.insert_one(forpass)
    collection.insert_one({"username":forname, "password":forpass})
    # file=open(username_info+".txt", "w")
    # file.write(username_info+"\n")
    # file.write(password_info)
    # file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    screen6 = Toplevel(window)
    screen6.title("Success")
    screen6.geometry("150x100")
    
    Label(screen6, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()


#--------------------LOGIN PAGE -----------------------


class LoginFile:

    def __init__(self, window):
        self.window = window
        self.window_width = 1166
        self.window_height = 718
        self.window.geometry(f'{self.window_width}x{self.window_height}+{100}+{30}')
        # self.window.geometry('1166x718')
        # self.window.state('zoomed')
        self.window.resizable(0, 0)

        
        global username_entry1
        global password_entry1
        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()

        #==========Background Image===========
        self.bg = Image.open('assets/bg/loginbg.png')
        photo = ImageTk.PhotoImage(self.bg)
        self.bgpan = Label(self.window, image=photo)
        self.bgpan.image = photo
        self.bgpan.pack(fill='both', expand='yes')

        self.loginbg = Image.open('assets/bg/login_bg.png')
        self.photo = ImageTk.PhotoImage(self.loginbg)
        self.loginframe = Label(self.window, image=self.photo, bg='#FFFFFF', width=950, height=600, borderwidth=0)
        self.loginframe.image = self.photo
        self.loginframe.place(x=200, y=70)

        # self.txt = 'WELCOME'
        # self.heading =  Label(self.loginframe, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#FFFFFF', fg='black')
        # self.heading.place(x=80, y=30, width=300, height=30)

        # self.CC = Image.open('assets/bg/COUNTME.png')
        # photo = ImageTk.PhotoImage(self.CC) 
        # self.CC_label = Label(self.loginframe, image=photo, bg='white')
        # self.CC_label.image = photo
        # self.CC_label.place(x=80, y=180)

        self.Logo = Image.open('assets/icons/CC.png')
        photo = ImageTk.PhotoImage(self.Logo)
        self.Logo_label = Label(self.loginframe, image=photo, bg='white')
        self.Logo_label.image = photo
        self.Logo_label.place(x=515, y=50)

        self.signin_label = Label(self.loginframe, text="Sign In", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        self.signin_label.place(x=688, y=190)


        #=============USERNAME==================
        username_icon = Image.open('assets/icons/user.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label= Label(self.loginframe, image=photo, bg='white')
        username_icon_label.image = photo
        username_icon_label.place(x=550, y=287)

        username_entry = Label(self.loginframe, text="Username", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        username_entry.place(x=550, y=240)
        username_entry1 = Entry(self.loginframe,  textvariable=username_verify,highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'))
        username_entry1.place(x=595, y=285, width=220)
        username_line = Canvas(self.loginframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
        username_line.place(x=580, y=309)

        #================PASSWORD===============================
        password_icon = Image.open('assets/icons/key.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label= Label(self.loginframe, image=photo, bg='white')
        password_icon_label.image = photo
        password_icon_label.place(x=550, y=387)

        password_entry = Label(self.loginframe, text="Password", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
        password_entry.place(x=550, y=340)
        password_entry1 = Entry(self.loginframe, textvariable=password_verify, highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'), show='*')
        password_entry1.place(x=595, y=385, width=320)
        self.password_line = Canvas(self.loginframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
        self.password_line.place(x=580, y=409)

        #=====================LOGIN BUTTON ===============================
        login_btn = Image.open('assets/placeholder/menu.png')
        photo = ImageTk.PhotoImage(login_btn)
        login_label= Label(self.loginframe, image=photo, bg='white')
        login_label.image = photo
        login_label.place(x=575, y=450)
        entry_button = Button(login_label, text='LOGIN', font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=login_verify)
        self.loginframe.bind('<Return>', login_verify)
        entry_button.place(x=40, y=10) 
        


        #======================REGISTER LOINK================
        register = Label(self.loginframe, text="No Account?", bg='white', fg='black', font=('yu gothic ui', 13, 'bold'))
        register.place(x=570, y=533)
        register_btn = Image.open('assets/placeholder/menu1.png')
        photo = ImageTk.PhotoImage(register_btn)
        register_label= Label(self.loginframe, image=photo, bg='white')
        register_label.image = photo
        register_label.place(x=675, y=530)
        register_button = Button(register_label, text='Register', font=('yu gothic ui', 10, 'bold'), width=10, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=regform)
        register_button.place(x=55, y=3)

        #===========================SHOW PASS=====================
        def show():
            show_btn1 = Image.open('assets/icons/eye.png')
            self.photo = ImageTk.PhotoImage(show_btn1)
            show_btn1 =  Button(self.window, image=self.photo, bd=0, bg='white', fg='black', cursor='hand2', command=show2)
            show_btn1.image = self.photo
            show_btn1.place(x=1050, y=452)
            password_entry1.config(show='')
    
        def show2():
            show_btn2 = Image.open('assets/icons/eye2.png')
            self.photo = ImageTk.PhotoImage(show_btn2)
            show_btn2 =  Button(self.window, image=self.photo,bd=0, bg='white', fg='black', cursor='hand2', command=show)
            show_btn2.image = self.photo
            show_btn2.place(x=1050, y=452)
            password_entry1.config(show='*')
            
        show_btn = Image.open('assets/icons/eye.png')
        self.photo = ImageTk.PhotoImage(show_btn)
        show_label= Button(self.window, image=self.photo, bd=0, bg='white', fg='black', cursor='hand2', command=show)
        show_label.image = photo
        show_label.place(x=1050, y=452)

        
#-----------------------REGISTER USER--------------------------------

def regform():

    global window

    window.geometry('1166x718')
    # window.state('zoomed')
    window.resizable(0, 0)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
        #==========Background Image===========
    bg = Image.open('assets/bg/loginbg.png')
    photo = ImageTk.PhotoImage(bg)
    bgpan = Label(window, image=photo)
    bgpan.image = photo
    bgpan.pack(fill='both', expand='yes')

    # regframe = Frame(window, bg='#FFFFFF', width=950, height=600, borderwidth=0)
    # regframe.pack()

    CC = Image.open('assets/bg/login_bg.png')
    photo = ImageTk.PhotoImage(CC) 
    regframe = Label(window, image=photo, bg='#FFFFFF', width=950, height=600, borderwidth=0)
    regframe.image = photo
    regframe.place(x=200, y=70)

    Logo = Image.open('assets/icons/CC.png')
    photo = ImageTk.PhotoImage(Logo)
    Logo_label = Label(regframe, image=photo, bg='white')
    Logo_label.image = photo
    Logo_label.place(x=515, y=50)

    signin_label = Label(regframe, text="Sign Un", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    signin_label.place(x=688, y=190)

    username_icon = Image.open('assets/icons/user.png')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label= Label(regframe, image=photo, bg='white')
    username_icon_label.image = photo
    username_icon_label.place(x=550, y=287)

    username_entry = Label(regframe, text="Username", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    username_entry.place(x=550, y=240)
    username_entry = Entry(regframe, textvariable = username, highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'))
    username_entry.place(x=595, y=285, width=220)
    username_line = Canvas(regframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
    username_line.place(x=580, y=309)

    password_icon = Image.open('assets/icons/key.png')
    photo = ImageTk.PhotoImage(password_icon)
    password_icon_label= Label(regframe, image=photo, bg='white')
    password_icon_label.image = photo
    password_icon_label.place(x=550, y=387)

    password_entry = Label(regframe, text="Password", bg='white', fg='black', font=('yu gothic ui', 17, 'bold'))
    password_entry.place(x=550, y=340)
    password_entry = Entry(regframe,  textvariable = password, highlightthickness=0, relief=FLAT, bg='white', fg='black', font=('yu gothic ui', 12, 'bold'), show='*')
    password_entry.place(x=595, y=385, width=320)
    password_line = Canvas(regframe, width=300, height=2.0, bg='#000000', highlightthickness=0)
    password_line.place(x=580, y=409)

    reg_btn = Image.open('assets/placeholder/menu.png')
    photo = ImageTk.PhotoImage(reg_btn)
    reg_label= Label(regframe, image=photo, bg='white')
    reg_label.image = photo
    reg_label.place(x=575, y=450)
    entry_button = Button(reg_label, text='REGISTER', font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25', command=register_user)
    entry_button.place(x=40, y=10)
    
    #===========================SHOW PASS=====================
    
    def show1():
        show_btn3 = Image.open('assets/icons/eye2.png')
        photo = ImageTk.PhotoImage(show_btn3)
        show_btn3 =  Button(window, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show3)
        show_btn3.image = photo
        show_btn3.place(x=1050, y=452)    
        password_entry.config(show='') 
    def show3():
        show_btn4 = Image.open('assets/icons/eye.png')
        photo = ImageTk.PhotoImage(show_btn4)
        show_btn4 =  Button(window, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show1)
        show_btn4.image = photo
        show_btn4.place(x=1050, y=452)
        password_entry.config(show='*')
            
    show_btn2 = Image.open('assets/icons/eye2.png')
    photo = ImageTk.PhotoImage(show_btn2)
    show_label2= Button(window, image=photo, bd=0, bg='white', fg='black', cursor='hand2', activebackground='white', command=show1)
    show_label2.image = photo
    show_label2.place(x=1050, y=452)        


#-----------------------------DASHBOARD -------------------------

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

        self.cam_text = Button(self.sidebar, text='Camera', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF', fg="#74B3BC", command=campage)
        self.cam_text.place(x=78, y=255)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_notif.image = photo
        self.logo_notif.place(x=37, y=325)

        self.notif_text = Button(self.sidebar, text='Gallery', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC", command=gallpage)
        self.notif_text.place(x=77, y=328)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=38, y=395)

        self.data_text = Button(self.sidebar, text='Database', bg='#132B2F', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC", command=datapage)
        self.data_text.place(x=78, y=398)


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

        dict_list = list( collection_name.find({"Date": f'{date:%A, %B %d, %Y}'}) )

        people_list = collection_name.find_one("Number")

        # self.bodyframe2 = Frame(self.file, bg="#253045", relief=GROOVE)
        # self.bodyframe2.place(x=380, y=435, width=269, height=80)

        # shss= collection_name.find_one()
        # self.poeple_Report = Label(self.bodyframe2, text='\n'.join([f"{k}: {v}" for k,v in shss.items()]), bg='#253045', font=("", 11, "bold"), fg='Black', anchor="center")
        # self.poeple_Report.place(x=13, y=10)

        # shss= collection_name.find_one()


        userframe= Image.open('assets/icons/asset 1.png')
        photo = ImageTk.PhotoImage(userframe)
        userframe1= Label(self.file, image=photo, bg='#B2CBC6')
        userframe1.image = photo
        userframe1.place(x=340, y=435)

        self.poeple_Report = Label(userframe1, text='Hi user, '+ username1, bg='#21CC82', font=("", 18, "bold"), fg='white', anchor="center")
        self.poeple_Report.place(x=4, y=10)

        # self.bodyframe3 =  Image.open('assets/icons/users.png')
        # photo = ImageTk.PhotoImage(self.bodyframe3)
        # self.users = Label(self.file, image=photo, bg="#B2CBC6")
        # self.users.image = photo
        # self.users.place(x=708, y=405)

    def changeLabel(self): 
            self.time2 = time.strftime('%H:%M:%S')
            self.watch.configure(text=self.time2)
            self.time_label.after(200, self.changeLabel) #it'll call itself continuously

#----------------------------CAMIIRA ---------------------------------------


notif = False
cappturee = False

def capvid():

    capframe = tk.Toplevel()
    capframe.title("COUNTME")
    capframe.geometry("1000x504")
    capframe.config(bg="#B2CBC6")

    # Label(capframe, text="Camera").pack()
    f1 = LabelFrame(capframe, bg="black")
    f1.pack()
    frame_num = 0
    l1 = Label(f1,bg="black")
    l1.pack()


    while True:
        centroid_dict = dict()
        
        rects = []
        ret, frame = cap.read()
        frame_num +=1
        height, width, channel = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)  
        net.setInput(blob)  
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4) 
        frame = frame.copy()
        
        center = list()
        rects = list()
        font = cv2.FONT_HERSHEY_PLAIN
        if len(indexes) > 0:
            idf = indexes.flatten()
                
            for i in idf:
                (x,y) = (boxes[i][0], boxes[i][1])
                (w,h) = (boxes[i][2], boxes[i][3])
                
                label = str(classes[class_ids[i]])
                
                if label == 'person':
                    center.append([int(x+w/2),int(y+h/2)])
                    # (startX,startY, endX,endY) = (x,y,x+w,y+h)
                    rects.append((x,y,w,h))
                                    
            boundingboxes = np.array(rects)
            
            boxes_ids = tracker.update(rects)
            for box_id in boxes_ids:
                (x,y,w,h,id)  = box_id
                Cx = int((x+x+w)/2)
                Cy = int((y+y+h)/2)
                centroid_dict[id] = (Cx,Cy,x,y,w,h)
            red_zone_dict = dict()
            
            for (id1, pt1),(id2,pt2) in combinations(centroid_dict.items(),2):
                dx,dy  = pt1[0]-pt2[0], pt1[1]-pt2[1]
                center_pair = [(pt1[0],pt1[1]),(pt2[0],pt2[1])]
            
                distance = np.sqrt(dx**2 + dy**2)
            
                if distance < 85:
                    if id1 not in red_zone_dict:
                        red_zone_dict[id1] = center_pair
                    if id2 not in red_zone_dict:
                        red_zone_dict[id2] = center_pair

            for id, box in centroid_dict.items():
                
                if id in red_zone_dict:

                    # height, width , channel = frame.shape
                    center_pair = red_zone_dict[id]
                    cv2.rectangle(frame, (box[2], box[3]), (box[4]+box[2],box[5]+box[3]), (0, 0, 255), 2)
                    cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2)

                    # tk.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
                    # toaster = ToastNotifier()
                    # toaster.show_toast("CountMe","Violation", duration=5, threaded=False)
                    current_timestamp = datetime.now().strftime("%Y-%m_%d-%I:%M:%S_%p")

                    if notif:
                            time.sleep(10)
                            toaster = ToastNotifier()
                            toaster.show_toast("CountMe","Violation", duration=5, threaded=False)

                    count = 0

                    if cappturee:
                            
                            ret, frame = cap.read(cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2))
                            faces = facedetect.detectMultiScale(frame, 1.3, 5)  

                            for x,y,w,h in faces:
                                count = count + 1
                                name='/Capture/'+ str(count) + '.png'
                                print("creating images ...." + name)
                                cv2.imwrite(name, frame[y:y+h,x:x+w])
                                cv2.rectangle(frame,(x,y), (x+w, y+h),(0,0,255), 2)
                                
                                with open(file, 'rb') as f:
                                    contents = f.read()
                                
                                fs.put(contents, filename=current_timestamp)   
                                
                                if count == 1 :   
                                    return

                    # crop_rate = 50 # capture images every so many frames (ex. crop photos every 150 frames)
                    # crop_path = os.path.join(os.getcwd(), 'detections', 'crop', video_name)
                    # try:
                    #     os.mkdir(crop_path)
                    # except FileExistsError:
                    #     pass
                    # if frame_num % crop_rate == 0:
                    # final_path = os.path.join(crop_path, 'frame_' + str(id))
                    # try:
                    #     os.mkdir(final_path)
                    # except FileExistsError:
                    #     pass          
                    # crop_objects(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), pred_bbox, final_path, classes[0])
                    
                    
                else:
                    cv2.rectangle(frame, (box[2], box[3]), (box[4]+box[2],box[5]+box[3]), (0, 255,0 ), 2)
                

                height, width , channel = frame.shape
                sub_img = frame[0:int(height/10),0:int(width)]
                
                black_rect = np.ones(sub_img.shape, dtype=np.uint8)*0
                
                res = cv2.addWeighted(sub_img,0.99,black_rect,0.20,0) 
                FONT = cv2.FONT_HERSHEY_SIMPLEX
                FONT_SCALE = 0.8
                FONT_THICKNESS = 2
                lable_color = (255, 255, 255)
                lable = "Persons:{}".format(len(center))
                lable_dimension = cv2.getTextSize(lable,FONT ,FONT_SCALE,FONT_THICKNESS)[0]
                textX = int((res.shape[1] - lable_dimension[0]) / 2)
                textY = int((res.shape[0] + lable_dimension[1]) / 2)
                lable2 = "Violation:{}".format(len(red_zone_dict))
                cv2.putText(res, lable, (textX,textY), FONT, FONT_SCALE, lable_color, FONT_THICKNESS)
                cv2.putText(res, "Violation:{}".format(len(red_zone_dict)), (0,textY+5+2), FONT,0.8, lable_color,2)

        # frame = cap.read()[1]
            imS = cv2.resize(frame, (540, 540))
            frame = cv2.cvtColor(imS, cv2.COLOR_BGR2RGB)
            frame = ImageTk.PhotoImage(Image.fromarray(frame))
            l1["image"] = frame

        def on_start():
            
            global notif
            notif = True
        def on_stop():
            global notif
            notif = False    

        def on_start2():
    
            global cappturee
            cappturee = True
        def on_stop2():
            global cappturee
            cappturee = False      

        start1_btn = Image.open('assets/icons/NOTIFY.png')
        photo = ImageTk.PhotoImage(start1_btn)
        start = Button(capframe, image=photo, command=on_start, bd=0,bg="#B2CBC6")
        start.image = photo
        start.place(x=5, y=0)

        stop1_btn = Image.open('assets/icons/STOP NOTIFICATION.png')
        photo = ImageTk.PhotoImage(stop1_btn)
        stop = Button(capframe, image=photo, command=on_stop, bd=0,bg="#B2CBC6")
        stop.image = photo
        stop.place(x=5, y=130)

        start2_btn = Image.open('assets/icons/CAPTURE.png')
        photo = ImageTk.PhotoImage(start2_btn)
        start2 = Button(capframe, image=photo, command=on_start2, bd=0,bg="#B2CBC6")
        start2.image = photo
        start2.place(x=5, y=270)

        stop2_btn = Image.open('assets/icons/STOP CAPTURE.png')
        photo = ImageTk.PhotoImage(stop2_btn)
        stop2 = Button(capframe, image=photo, command=on_stop2,bg="#B2CBC6", bd=0)
        stop2.image = photo
        stop2.place(x=5, y=420)

        reg_btn = Image.open('assets/icons/PERSONS DETECTED CONTAINER.png')
        photo = ImageTk.PhotoImage(reg_btn)
        reg_label= Label(capframe, image=photo, bg='#B2CBC6')
        reg_label.image = photo
        reg_label.place(x=775, y=10)
        entry_button = Label(reg_label, text=lable, font=('yu gothic ui', 15, 'bold'), width=10, bd=0, bg='#9FFF95', fg='black', cursor='hand2', activebackground='#0b2b25')
        entry_button.place(x=80, y=15)

        reg_btn2 = Image.open('assets/icons/VIOLATIONS DETECTED.png')
        photo = ImageTk.PhotoImage(reg_btn2)
        reg_label2= Label(capframe, image=photo, bg='#B2CBC6')
        reg_label2.image = photo
        reg_label2.place(x=775, y=140)
        entry_button2 = Label(reg_label2, text=lable2, font=('yu gothic ui', 15, 'bold'), width=10, bd=0, bg='#FF6B6B', fg='black', cursor='hand2', activebackground='#0b2b25')
        entry_button2.place(x=80, y=15)

        capframe.update()
        
class Camiira:  
    def __init__(self, cammish):
        self.cammish = cammish
        self.cammish_width = 1040
        self.cammish_height = 640
        self.cammish.geometry(f'{self.cammish_width}x{self.cammish_height}+{100}+{30}')
        self.cammish.config(background="#B2CBC6")
        self.cammish.resizable(0,0)
        

        icon = PhotoImage(file='assets/icons/CC2.png')
        self.cammish.iconphoto(True, icon)

         #===========HEADER==========
        self.time_holder= Image.open('assets/icons/TIME PLACEHOLDER.png')
        photo = ImageTk.PhotoImage(self.time_holder)
        self.time_label= Label(self.cammish, image=photo, bg="#B2CBC6")
        self.time_label.image = photo
        self.time_label.place(x=700, y=0) 
        
        #=========NAVBAR===============
        self.sidebar = Frame(self.cammish, bg="#132B2F")
        self.sidebar.place(x=0, y=0, width=275, height=750)

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
        # self.heading = Label(self.cammish, text='Camera', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        # self.heading.place(x=325, y=70)

        # def cammo():

        #     v = main()
        #     v.video = webcam.Box(self.cammish, width=450, height=450)
        #     v.video.show_frames()

        # self.cam= Button(self.cammish, command=cammo)
        # self.cam.place(x=708, y=435)  

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=35, y=255)

        self.dash_text = Button(self.sidebar, text='Dashboard', 
            bg='#132B2F', font=("", 13, "bold"), fg="#74B3BC",
            bd=0, cursor='hand2', activebackground='#132B2F',
            command=backtodash)
        self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/CAMERA SELECTED.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=10, y=295)

        # self.cam_text = Button(self.sidebar, text='Camera', bg='#FFFFFF', font=("", 13, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF')
        # self.cam_text.place(x=75, y=315)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_notif.image = photo
        self.logo_notif.place(x=35, y=365)

        self.notif_text = Button(self.sidebar, text='Gallery', bg='#132B2F', font=("", 13, "bold"), bd=0,fg="#74B3BC", cursor='hand2', activebackground='#FFFFFF', command=backtogall)
        self.notif_text.place(x=75, y=368)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=35, y=415)

        self.data_text = Button(self.sidebar, text='Database', bg='#132B2F', font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground='#FFFFFF', command=backtodata)
        self.data_text.place(x=75, y=418)
        
        self.logout = Image.open('assets/icons/logout.png')
        photo = ImageTk.PhotoImage(self.logout)
        self.logout_btn = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logout_btn.image = photo
        self.logout_btn.place(x=38, y=545)

        self.logout_text = Button(self.sidebar, text='Logout', bg='#132B2F', font=("", 18, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.logout_text.place(x=95, y=548)
        # def cammo():
            
        #     v = findObjects()
        #     v.video = webcam.Box(self.cammish, width=450, height=450)
        #     v.video.show_frames()

        self.logo_dash = Image.open('assets/icons/WIDGET - CONNECT TO CAM.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.cammish, image=photo, bg="#B2CBC6")
        self.logo_dash.image = photo
        self.logo_dash.place(x=325, y=80)


        v = capvid
        
        self.cam_btn = Image.open('assets/icons/CONNECT TO CAMERA.png')
        photo = ImageTk.PhotoImage(self.cam_btn)
        self.cam_label= Button(self.cammish, image=photo, bg="#B2CBC6", bd=0, activebackground="#B2CBC6")
        self.cam_label['command'] = v
        self.cam_label.image = photo
        self.cam_label.place(x=550, y=520) 
        # self.cam = Button(cam_label, font=('yu gothic ui', 12, 'bold'), width=25, bd=0, bg='#0b2b25', fg='white', cursor='hand2', activebackground='#0b2b25')
        # self.cam['command'] = v
        # self.cam.place(x=8, y=5) 

    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.time_label.after(200, self.changeLabel) #it'll call itself continuously
        
#-----------------------------GALLERY-----------------------------------


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

        #==========LOGO NAME=========
        # self.brandName = Label(self.sidebar, text='CountMe', bg='#FFFFFF', font=("", 13, "bold"))
        # self.brandName.place(x=80, y=150)

        self.logout = Image.open('assets/icons/logout.png')
        photo = ImageTk.PhotoImage(self.logout)
        self.logout_btn = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logout_btn.image = photo
        self.logout_btn.place(x=38, y=545)

        self.logout_text = Button(self.sidebar, text='Logout', bg='#132B2F', font=("", 18, "bold"), bd=0, cursor='hand2', activebackground='#FFFFFF',fg="#74B3BC")
        self.logout_text.place(x=95, y=548)

        #=========CONTENTS =============
        self.heading = Label(self.pish, text='Galleria', font=("", 13, "bold"), fg='Black', bg="#B0AEAE")
        self.heading.place(x=325, y=70)

        self.logo_dash = Image.open('assets/icons/pps.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=38, y=150)

        self.dash_text = Label(self.sidebar, text='Dashboard',  bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F")
        self.dash_text.place(x=80, y=158)

        self.dash_text = Button(self.sidebar, text='Dashboard', 
           bg="#132B2F", font=("", 13, "bold"), 
            bd=0, cursor='hand2', activebackground="#132B2F",
            command=backtodash)

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo,bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=38, y=230)

        self.cam_text = Button(self.sidebar, text='Camera', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F", command=backtocam)
        self.cam_text.place(x=78, y=235)

        self.logo_dash = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=10, y=300)

        self.notif_text = Button(self.sidebar, text='Gallery', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F", command=backtogall)
        self.notif_text.place(x=75, y=368)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=38, y=395)

        self.data_text = Button(self.sidebar, text='Database', bg="#132B2F", font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground="#132B2F", command=backtodata)
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

            


#-----------------------------DATABASE ---------------------------------

class Database:
    def __init__(self, records):

        self.records = records
        self.file_width = 1040
        self.file_height = 640
        self.records.geometry(f'{self.file_width}x{self.file_height}+{100}+{30}')
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

        self.dash_text = Button(self.sidebar, text='Dashboard', 
            bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', 
            bd=0, cursor='hand2', activebackground='#132B2F',
            command=backtodash)
        self.dash_text.place(x=80, y=262)

        self.logo_cam = Image.open('assets/icons/camera.png')
        photo = ImageTk.PhotoImage(self.logo_cam)
        self.logo_cam = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_cam.image = photo
        self.logo_cam.place(x=35, y=310)

        self.cam_text = Button(self.sidebar, text='Camera', bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', bd=0, cursor='hand2', activebackground='#FFFFFF', command=backtocam)
        self.cam_text.place(x=75, y=315)

        self.logo_notif = Image.open('assets/icons/ss.png')
        photo = ImageTk.PhotoImage(self.logo_notif)
        self.logo_notif = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_notif.image = photo
        self.logo_notif.place(x=35, y=365)

        self.notif_text = Button(self.sidebar, text='Gallery', bg='#132B2F', font=("", 13, "bold"), fg='#74B3BC', bd=0, cursor='hand2', activebackground='#FFFFFF', command=backtogall)
        self.notif_text.place(x=75, y=368)

        self.logo_dash = Image.open('assets/icons/DATABASE SELECTED.png')
        photo = ImageTk.PhotoImage(self.logo_dash)
        self.logo_dash = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_dash.image = photo
        self.logo_dash.place(x=10, y=415)


        #========FOR TABLES==============
        self.bodyframe1 = Frame(self.records, bg="#FFFFFF")
        
        self.bodyframe1.place(x=328, y=110, width=1040, height=590)
        
        serts = StringVar()

        def sertz():
            
            datee = self.search.get()

            dict_list = list( collection_name1.find({"Date": datee}) )
            
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

            # scroll = Scrollbar(self.bodyframe1, orient='vertical', command=doc)
            # scroll.grid(row=0, column=1, sticky='ns')
            # dict_list['yscrollcommand'] = scroll.set

        self.search = Image.open('assets/icons/DATABASE WIDGET.png')
        photo = ImageTk.PhotoImage(self.search)
        self.search_label= Label(self.records, image=photo, bg='#B2CBC6')
        self.search_label.image = photo
        self.search_label.place(x=305, y=0)
        
        self.search = Entry(self.search_label, textvariable = serts, bg="#FFFFFF",width=30)
        self.search.insert(0, '(Date. ex. Friday, then (M/D/Y)')
        self.search.place(x=190, y=30)
        self.sertsbtn = Button(self.search_label, text = "Search", width = 10, height = 1, command = sertz).place(x=400, y=25)


def page():
    global window
    window = tk.Tk()
    window.geometry("800x604")
    window.config(bg="#071D20")
    LoginFile(window)
    window.mainloop()            

if __name__ == '__main__':
    page()
