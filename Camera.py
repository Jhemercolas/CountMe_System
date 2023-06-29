from gettext import find
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from turtle import shape
from typing import Any
from PIL import Image, ImageTk
import gridfs
import subprocess
import numpy as image_np
import numpy as np
import json
import requests
import base64
from sqlalchemy import create_engine
from win10toast import ToastNotifier
# from photoboothapp import Capvideo
import cv2
import PySimpleGUI as sg
import os
from tkinter import ttk
import sys
from keras.models import load_model
import tensorflow
import pymongo
from pymongo import MongoClient
from importlib.machinery import SourceFileLoader
import pandas as pd
from itertools import combinations
import time
from trackPerson import EuclideanDistTracker
import datetime as dt
from non_max_suppression import non_max_suppression_fast
import mss as miss
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime
date = dt.datetime.now()

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

appsIcon = (Image.open("assets/icons/pps.png"))
# path = sys.path.append('C:\Users\Client\OneDrive\Documents\Python projects\CountMe - main\home.py')

cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")

# try:
#     cluster = MongoClient("mongodb+srv://jhemercris_colas:Smartbro10@mycluster.itjla.mongodb.net/?retryWrites=true&w=majority")
#     cluster.server_info()
# except pymongo.errors.ServerSelectionTimeoutError as err:
#     print(err)

tracker = EuclideanDistTracker()
wht = 1000
confThreshold = 0.3
nmsThreshold = 0.3

# db = cluster["camera"]
# dbb = db["images"]

db = cluster["Reports"]
collection_name = db["Violators"]

fs = gridfs.GridFS(db)
file = "C:/Users/Client/OneDrive/Documents/Python projects/New folder/Capture/1.jpeg"

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

cap = cv2.VideoCapture('C:/Users/Client/OneDrive/Documents/Python projects/New folder/sample footage/CBM.mp4')
# cap = cv2.VideoCapture(0)
output_layers = net.getUnconnectedOutLayersNames()
print(output_layers)

current_timestamp = datetime.now().strftime("%Y-%m_%d-%I:%M:%S_%p")

# post = {"_id": 0, "name": "Violators", "score": 1}
# collection_name.insert_one(post)
                
# class Cv:
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
            
                if distance < 200:
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

                    # if notif:
                        
                    #         time.sleep(5)
                    #         toaster = ToastNotifier()
                    #         toaster.show_toast("CountMe","Violation", duration=5, threaded=False)

                    

                    # if cappturee:
                    count = 0
                    while True:
                            
                        ret, frame = cap.read(cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2))
                        faces = facedetect.detectMultiScale(frame, 1.3, 5)  

                        for x,y,w,h in faces:
                            count = count + 1
                            name='/Capture/'+ str(count) + '.jpeg'
                            print("creating images ...." + name)
                            cv2.imwrite(name, frame[y:y+h,x:x+w])
                            cv2.rectangle(frame,(x,y), (x+w, y+h),(0,0,255), 2)
                            
                            with open(file, 'rb') as f:
                                contents = f.read()
                            
                            fs.put(contents, filename=current_timestamp)   
                                
                                # if count == 1 :   
                                #     return

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
                cv2.putText(res, lable, (textX,textY), FONT, FONT_SCALE, lable_color, FONT_THICKNESS)
                cv2.putText(res, "Violation:{}".format(len(red_zone_dict)), (0,textY+5+2), FONT,0.8, lable_color,2)

           
            
    # frame = cap.read()[1]
            imS = cv2.resize(frame, (540, 540))
            frame = cv2.cvtColor(imS, cv2.COLOR_BGR2RGB)
            frame = ImageTk.PhotoImage(Image.fromarray(frame))
            l1["image"] = frame

            lable2 = "Violation:{}".format(len(red_zone_dict))
                    
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
            )
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

        self.notif_text = Button(self.sidebar, text='Notification', bg='#132B2F', font=("", 13, "bold"), bd=0,fg="#74B3BC", cursor='hand2', activebackground='#FFFFFF')
        self.notif_text.place(x=75, y=368)

        self.logo_data = Image.open('assets/icons/dd.png')
        photo = ImageTk.PhotoImage(self.logo_data)
        self.logo_data = Label(self.sidebar, image=photo, bg="#132B2F")
        self.logo_data.image = photo
        self.logo_data.place(x=35, y=415)

        self.data_text = Button(self.sidebar, text='Database', bg='#132B2F', font=("", 13, "bold"),fg="#74B3BC", bd=0, cursor='hand2', activebackground='#FFFFFF')
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
        
            
def win():
    global cammish
    cammish = Tk()
    cammish.geometry("800x604")
    cammish.config(bg="#071D20")
    Camiira(cammish) 
    cammish.mainloop()

if __name__ == '__main__':
    win()
