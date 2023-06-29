import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from trackPerson import EuclideanDistTracker
import tkinter as tk
from datetime import datetime
from non_max_suppression import non_max_suppression_fast
from itertools import combinations
# import sys
# if "tkinter" not in sys.modules:
#     from tkinter import *




facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capframe = Tk()
capframe.title("COUNTME")
capframe.geometry("1000x504")
capframe.config(bg="#071D20")

tracker = EuclideanDistTracker()
wht = 1000
confThreshold = 0.3
nmsThreshold = 0.3

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

# cap = cv2.VideoCapture('sample footage/CULTURAL COC.mp4')
# cap = cv2.VideoCapture(0)
output_layers = net.getUnconnectedOutLayersNames()
print(output_layers)

Label(capframe, text="Camera").pack()
f1 = LabelFrame(capframe, bg="black")
f1.pack()

l1 = Label(f1,bg="black")
l1.pack()

cap = cv2.VideoCapture('sample footage/CULTURAL COC.mp4')
# cap = cv2.VideoCapture(0)
frame_num = 0
centroid_dict = dict()
print(centroid_dict)
current_timestamp = datetime.now().strftime("%Y-%m_%d-%I:%M:%S_%p")

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
        
            if distance < 300:
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
                # while True:
                #     time.sleep(5)
                #     toaster = ToastNotifier()
                #     toaster.show_toast("CountMe","Violation", duration=5, threaded=False)
                #     break

                # count = 0
                # while True:
                        
                #         ret, frame = cap.read(cv2.line(frame,center_pair[0], center_pair[1],(0,0,255),2))
                #         faces = facedetect.detectMultiScale(frame, 1.3, 5)  

                #         for x,y,w,h in faces:
                #             count = count + 1
                #             name='./Capture/'+ str(count) + '.png'
                #             print("creating images ...." + name)
                #             cv2.imwrite(name, frame[y:y+h,x:x+w])
                #             cv2.rectangle(frame,(x,y), (x+w, y+h),(0,0,255), 2)
                            
                #             with open(file, 'rb') as f:
                #                 contents = f.read()
                            
                #             fs.put(contents, filename=current_timestamp)   
                            
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
            lable2 = "Violation:{}".format(len(red_zone_dict))
            cv2.putText(res, lable, (textX,textY), FONT, FONT_SCALE, lable_color, FONT_THICKNESS)
            cv2.putText(res, "Violation:{}".format(len(red_zone_dict)), (0,textY+5+2), FONT,0.8, lable_color,2)

    # frame = cap.read()[1]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(Image.fromarray(frame))
        l1["image"] = frame
    capframe.update()
