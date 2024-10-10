#written by Amay Singh
import cv2
import mediapipe as mp
import numpy as np
from datetime import datetime
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

import tkinter as tk
cap = cv2.imread("r_img2.jpg") #input image path here
root=tk.Tk()
 
# setting the windows size

root.geometry("800x600")
  
# declaring string variable
# for storing name and password
twist=tk.StringVar()
load=tk.StringVar()
time=tk.StringVar()
leg=tk.StringVar()
arm=tk.StringVar()
neck_twist=tk.StringVar()

neck_bend=tk.StringVar()
side=tk.StringVar()
trunk_twist=tk.StringVar()

trunk_bend=tk.StringVar()
couple=tk.StringVar()
name_label = tk.Label(root, text = 'Wrist twist (0-2)', font=('calibre',12, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = twist, font=('calibre',12,'normal'))
  

passw_label = tk.Label(root, text = 'Load/Force (lbs)', font = ('calibre',12,'bold'))
  

passw_entry=tk.Entry(root, textvariable = load, font = ('calibre',12,'normal'))
  
pass_label = tk.Label(root, text = 'Duration (min)', font = ('calibre',12,'bold'))
  

pass_entry=tk.Entry(root, textvariable = time, font = ('calibre',12,'normal'))
pass_label2 = tk.Label(root, text = 'Leg Support (1-2)', font = ('calibre',12,'bold'))

  

pass_entry2=tk.Entry(root, textvariable = leg, font = ('calibre',12,'normal'))
pass_label9 = tk.Label(root, text = 'Arm Support (1-2)', font = ('calibre',12,'bold'))

  

pass_entry9=tk.Entry(root, textvariable = arm, font = ('calibre',12,'normal'))
pass_label3 = tk.Label(root, text = 'Neck Twist (0-1)', font = ('calibre',12,'bold'))
  

pass_entry3=tk.Entry(root, textvariable = neck_twist, font = ('calibre',12,'normal'))
pass_label4 = tk.Label(root, text = 'Neck Bend (0-1)', font = ('calibre',12,'bold'))
  

pass_entry4=tk.Entry(root, textvariable = neck_bend, font = ('calibre',12,'normal'))
pass_label6 = tk.Label(root, text = 'Trunk bend (0-1)', font = ('calibre',12,'bold'))
  

pass_entry6=tk.Entry(root, textvariable = trunk_bend, font = ('calibre',12,'normal'))
pass_label7= tk.Label(root, text = 'Trunk twist(0-1)', font = ('calibre',12,'bold'))
  

pass_entry7=tk.Entry(root, textvariable = trunk_twist, font = ('calibre',12,'normal'))
pass_label8= tk.Label(root, text = 'Coupling score', font = ('calibre',12,'bold'))
  

pass_entry8=tk.Entry(root, textvariable = couple, font = ('calibre',12,'normal'))
pass_label5 = tk.Label(root, text = 'R/L', font = ('calibre',12,'bold'))
  

pass_entry5=tk.Entry(root, textvariable = side, font = ('calibre',12,'normal'))
sub_btn=tk.Button(root,text = 'Submit',font = ('calibre',12,'normal'), command = root.destroy)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
pass_label.grid(row=2,column=0)
pass_entry.grid(row=2,column=1)
pass_label2.grid(row=3,column=0)
pass_entry2.grid(row=3,column=1)
pass_label3.grid(row=4,column=0)
pass_entry3.grid(row=4,column=1)
pass_label4.grid(row=5,column=0)
pass_entry4.grid(row=5,column=1)
pass_label6.grid(row=6,column=0)
pass_entry6.grid(row=6,column=1)
pass_label7.grid(row=7,column=0)
pass_entry7.grid(row=7,column=1)
pass_label8.grid(row=8,column=0)
pass_entry8.grid(row=8,column=1)
pass_label9.grid(row=9,column=0)
pass_entry9.grid(row=9,column=1)
pass_label5.grid(row=10,column=0)
pass_entry5.grid(row=10,column=1)


sub_btn.grid(row=11,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()

from tkinter import *
class Table:
     
    def __init__(self,root,lst,r):
         
        # code for creating table
        for i in range(r):
            for j in range(3):
                if(j<2):
                    self.e = Entry(root, width=20, fg='blue',
                                font=('Arial',16,'bold'))
                else:
                    self.e = Entry(root, width=45, fg='blue',
                                font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
t1=datetime.now()
h,w,c=cap.shape
print(h,w)
y,x=h,w
dd=1
z=min(x,y)
z2=max(x,y)
if(z<600):
     dd=600/z 
if(z2>800):
     dd=800/z2



#cap = cv2.resize(cap,(x,y))
cap= cv2.resize(cap, (0,0), fx = dd, fy = dd)
y,x,c=cap.shape
print(x,y)
#calculation of score following conditions of rula tables
def rulaC(uarm,larm,wrist,wrist_twist,duration,force,leg,neck,trunk,neck_bend,neck_twist,trunk_bend,trunk_twist):
    rula=0
    if(uarm==1):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=1 
                    else:
                        rula=2 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=2 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=2 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=2 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=3 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
    elif(uarm==2):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
    elif(uarm==3):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
    elif(uarm==4):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6
    elif(uarm==5):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=5 
                    else:
                        rula=6
                else:
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=7
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=6
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=7
                else:
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=6 
                    else:
                        rula=7 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
                else:
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=8
    elif(uarm==6):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=7 
                    else:
                        rula=7 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=8
                else:
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=9
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=8
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=8
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=9
                else:
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=9 
                    else:
                        rula=9
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
                else:
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
    if(force<4.4):
        rula+=0
    elif(force<22):
        rula+=1
    else:
        rula+=3

    if(duration>4):
        rula+=1 
    x=0
    if(neck_twist==1):
        neck+=1
    if(neck_bend==1):
        neck+=1
    if(trunk_twist==1):
        trunk+=1
    if(trunk_bend==1):
        trunk+=1
    if(neck==1):
        if(trunk==1):
            if(leg==1):
                x=1
            else:
                x=3 
        elif(trunk==2):
            if(leg==1):
                x=2
            else:
                x=3 
        elif(trunk==3):
            if(leg==1):
                x=3
            else:
                x=4
        elif(trunk==4):
            if(leg==1):
                x=5
            else:
                x=5
        elif(trunk==5):
            if(leg==1):
                x=6
            else:
                x=6
        else:
            if(leg==1):
                x=7
            else:
                x=7
    elif(neck==2):
        if(trunk==1):
            if(leg==1):
                x=2
            else:
                x=3 
        elif(trunk==2):
            if(leg==1):
                x=2
            else:
                x=3 
        elif(trunk==3):
            if(leg==1):
                x=4
            else:
                x=5
        elif(trunk==4):
            if(leg==1):
                x=5
            else:
                x=5
        elif(trunk==5):
            if(leg==1):
                x=6
            else:
                x=7
        else:
            if(leg==1):
                x=7
            else:
                x=7
    elif(neck==3):
        if(trunk==1):
            if(leg==1):
                x=3
            else:
                x=3 
        elif(trunk==2):
            if(leg==1):
                x=3
            else:
                x=4
        elif(trunk==3):
            if(leg==1):
                x=4
            else:
                x=5
        elif(trunk==4):
            if(leg==1):
                x=5
            else:
                x=6
        elif(trunk==5):
            if(leg==1):
                x=6
            else:
                x=7
        else:
            if(leg==1):
                x=7
            else:
                x=7
    elif(neck==4):
        if(trunk==1):
            if(leg==1):
                x=5
            else:
                x=5
        elif(trunk==2):
            if(leg==1):
                x=5
            else:
                x=6
        elif(trunk==3):
            if(leg==1):
                x=6
            else:
                x=7
        elif(trunk==4):
            if(leg==1):
                x=7
            else:
                x=7
        elif(trunk==5):
            if(leg==1):
                x=7
            else:
                x=7
        else:
            if(leg==1):
                x=8
            else:
                x=8
    elif(neck==5):
        if(trunk==1):
            if(leg==1):
                x=7
            else:
                x=7
        elif(trunk==2):
            if(leg==1):
                x=7
            else:
                x=7
        elif(trunk==3):
            if(leg==1):
                x=7
            else:
                x=8
        elif(trunk==4):
            if(leg==1):
                x=8
            else:
                x=8
        elif(trunk==5):
            if(leg==1):
                x=8
            else:
                x=8
        else:
            if(leg==1):
                x=8
            else:
                x=8
    else:
        if(trunk==1):
            if(leg==1):
                x=8
            else:
                x=8
        elif(trunk==2):
            if(leg==1):
                x=8
            else:
                x=8
        elif(trunk==3):
            if(leg==1):
                x=8
            else:
                x=8
        elif(trunk==4):
            if(leg==1):
                x=8
            else:
                x=9
        elif(trunk==5):
            if(leg==1):
                x=9
            else:
                x=9
        else:
            if(leg==1):
                x=9
            else:
                x=9
    if(rula==1):
        if(x==1):
            rula=1
        elif(x==2):
            rula=2
        elif(x==3):
            rula=3
        elif(x==4):
            rula=3
        elif(x==5):
            rula=4
        elif(x==6):
            rula=5
        else:
            rula=5
    elif(rula==2):
        if(x==1):
            rula=2
        elif(x==2):
            rula=2
        elif(x==3):
            rula=3
        elif(x==4):
            rula=4
        elif(x==5):
            rula=4
        elif(x==6):
            rula=5
        else:
            rula=5
    elif(rula==3):
        if(x==1):
            rula=3
        elif(x==2):
            rula=3
        elif(x==3):
            rula=3
        elif(x==4):
            rula=4
        elif(x==5):
            rula=4
        elif(x==6):
            rula=5
        else:
            rula=6
    elif(rula==4):
        if(x==1):
            rula=3
        elif(x==2):
            rula=3
        elif(x==3):
            rula=3
        elif(x==4):
            rula=4
        elif(x==5):
            rula=5
        elif(x==6):
            rula=6
        else:
            rula=6
    elif(rula==5):
        if(x==1):
            rula=4
        elif(x==2):
            rula=4
        elif(x==3):
            rula=4
        elif(x==4):
            rula=5
        elif(x==5):
            rula=6
        elif(x==6):
            rula=7
        else:
            rula=7
            rula=6
    elif(rula==6):
        if(x==1):
            rula=4
        elif(x==2):
            rula=4
        elif(x==3):
            rula=5
        elif(x==4):
            rula=6
        elif(x==5):
            rula=6
        elif(x==6):
            rula=7
        else:
            rula=7
    elif(rula==7):
        if(x==1):
            rula=5
        elif(x==2):
            rula=5
        elif(x==3):
            rula=6
        elif(x==4):
            rula=6
        elif(x==5):
            rula=7
        elif(x==6):
            rula=7
        else:
            rula=7
    else:
        if(x==1):
            rula=5
        elif(x==2):
            rula=5
        elif(x==3):
            rula=6
        elif(x==4):
            rula=7
        elif(x==5):
            rula=7
        elif(x==6):
            rula=7
        else:
            rula=7
    
    return rula
#calculation of score following conditions of reba tables
def rebaC(uarm,larm,wrist,wrist_twist,duration,force,leg,neck,trunk,neck_bend,neck_twist,trunk_bend,trunk_twist,couple,knee):
    rula=0
    if(uarm==1):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=1 
                    else:
                        rula=2 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=2 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=2 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=2 
                    else:
                        rula=2 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=3 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
    elif(uarm==2):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=2
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=3 
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
    elif(uarm==3):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=3
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=3
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
    elif(uarm==4):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=4 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=4
                    else:
                        rula=4 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=4 
                    else:
                        rula=5 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
                else:
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6
    elif(uarm==5):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=5 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=5 
                    else:
                        rula=6
                else:
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=7
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=5
                    else:
                        rula=6
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=7
                else:
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=6
                    else:
                        rula=6 
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=6 
                    else:
                        rula=7 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
                else:
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=8
    elif(uarm==6):
            if(larm==1):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=7
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=7 
                    else:
                        rula=7 
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=7
                    else:
                        rula=8
                else:
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=9
            elif(larm==2):
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=8
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=8
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=8
                    else:
                        rula=9
                else:
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
            else:
                if(wrist==1):
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
                elif(wrist==2):
                    if(wrist_twist==1):
                        rula=9 
                    else:
                        rula=9
                elif(wrist==3):
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
                else:
                    if(wrist_twist==1):
                        rula=9
                    else:
                        rula=9
    

    
    rula+=couple
    x=0
    if(neck_twist==1):
        neck+=1
    if(neck_bend==1):
        neck+=1
    if(trunk_twist==1):
        trunk+=1
    if(trunk_bend==1):
        trunk+=1
    reba=0
    if(neck==1):
        if(trunk==1):
            if(knee==1):
                x=1
            elif(knee==2):
                x=2
            elif(knee==3):
                x=3
            else:
                x=4
            
        elif(trunk==2):
            if(knee==1):
                x=2
            elif(knee==2):
                x=3
            elif(knee==3):
                x=4
            else:
                x=5
        elif(trunk==3):
            if(knee==1):
                x=2
            elif(knee==2):
                x=4
            elif(knee==3):
                x=5
            else:
                x=6
        
        elif(trunk==4):
            if(knee==1):
                x=3
            elif(knee==2):
                x=5
            elif(knee==3):
                x=6
            else:
                x=7
        else:
            if(knee==1):
                x=4
            elif(knee==2):
                x=6
            elif(knee==3):
                x=7
            else:
                x=8
        
    elif(neck==2):
        if(trunk==1):
            if(knee==1):
                x=1
            elif(knee==2):
                x=2
            elif(knee==3):
                x=3
            else:
                x=4
            
        elif(trunk==2):
            if(knee==1):
                x=3
            elif(knee==2):
                x=4
            elif(knee==3):
                x=5
            else:
                x=6
        
        elif(trunk==3):
            if(knee==1):
                x=4
            elif(knee==2):
                x=5
            elif(knee==3):
                x=6
            else:
                x=7
        elif(trunk==4):
            if(knee==1):
                x=5
            elif(knee==2):
                x=6
            elif(knee==3):
                x=7
            else:
                x=8
        else:
            if(knee==1):
                x=6
            elif(knee==2):
                x=7
            elif(knee==3):
                x=8
            else:
                x=9
    else:
        if(trunk==1):
            if(knee==1):
                x=3
            elif(knee==2):
                x=3
            elif(knee==3):
                x=5
            else:
                x=6
            
        elif(trunk==2):
            if(knee==1):
                x=4
            elif(knee==2):
                x=5
            elif(knee==3):
                x=6
            else:
                x=7
        elif(trunk==3):
            if(knee==1):
                x=5
            elif(knee==2):
                x=6
            elif(knee==3):
                x=7
            else:
                x=8
        elif(trunk==4):
            if(knee==1):
                x=6
            elif(knee==2):
                x=7
            elif(knee==3):
                x=8
            else:
                x=9
        else:
            if(knee==1):
                x=7
            elif(knee==2):
                x=8
            elif(knee==3):
                x=9
            else:
                x=9
    if(force<=11):
        x+=0
    elif(force<=22):
        x+=1
    else:
        x+=2
    if(x==1):
        if(rula==1):
            reba=1
        elif(rula==2):
            reba=1
        elif(rula==3):
            reba=1
        elif(rula==4):
            reba=2
        elif(rula==5):
            reba=3
        elif(rula==6):
            reba=3
        elif(rula==7):
            reba=4
        elif(rula==8):
            reba=5
        elif(rula==9):
            reba=6
        elif(rula==10):
            reba=7
        elif(rula==11):
            reba=7
        else:
            reba=7 
    elif(x==2):
        if(rula==1):
            reba=1
        elif(rula==2):
            reba=2
        elif(rula==3):
            reba=2
        elif(rula==4):
            reba=3
        elif(rula==5):
            reba=4
        elif(rula==6):
            reba=4
        elif(rula==7):
            reba=5
        elif(rula==8):
            reba=6
        elif(rula==9):
            reba=6
        elif(rula==10):
            reba=7
        elif(rula==11):
            reba=7
        else:
            reba=8
    elif(x==3):
        if(rula==1):
            reba=2
        elif(rula==2):
            reba=3
        elif(rula==3):
            reba=3
        elif(rula==4):
            reba=3
        elif(rula==5):
            reba=4
        elif(rula==6):
            reba=5
        elif(rula==7):
            reba=6
        elif(rula==8):
            reba=7
        elif(rula==9):
            reba=7
        elif(rula==10):
            reba=8
        elif(rula==11):
            reba=8
        else:
            reba=8
    elif(x==4):
        if(rula==1):
            reba=3
        elif(rula==2):
            reba=4
        elif(rula==3):
            reba=4
        elif(rula==4):
            reba=4
        elif(rula==5):
            reba=5
        elif(rula==6):
            reba=6
        elif(rula==7):
            reba=7
        elif(rula==8):
            reba=8
        elif(rula==9):
            reba=8
        elif(rula==10):
            reba=9
        elif(rula==11):
            reba=9
        else:
            reba=9
    elif(x==5):
        if(rula==1):
            reba=4
        elif(rula==2):
            reba=4
        elif(rula==3):
            reba=4
        elif(rula==4):
            reba=5
        elif(rula==5):
            reba=6
        elif(rula==6):
            reba=7
        elif(rula==7):
            reba=8
        elif(rula==8):
            reba=8
        elif(rula==9):
            reba=9
        elif(rula==10):
            reba=9
        elif(rula==11):
            reba=9
        else:
            reba=9
    elif(x==6):
        if(rula==1):
            reba=6
        elif(rula==2):
            reba=6
        elif(rula==3):
            reba=6
        elif(rula==4):
            reba=7
        elif(rula==5):
            reba=8
        elif(rula==6):
            reba=8
        elif(rula==7):
            reba=9
        elif(rula==8):
            reba=9
        elif(rula==9):
            reba=10
        elif(rula==10):
            reba=10
        elif(rula==11):
            reba=10
        else:
            reba=10
    elif(x==7):
        if(rula==1):
            reba=7
        elif(rula==2):
            reba=7
        elif(rula==3):
            reba=7
        elif(rula==4):
            reba=8
        elif(rula==5):
            reba=9
        elif(rula==6):
            reba=9
        elif(rula==7):
            reba=9
        elif(rula==8):
            reba=10
        elif(rula==9):
            reba=10
        elif(rula==10):
            reba=11
        elif(rula==11):
            reba=11
        else:
            reba=11
    elif(x==8):
        if(rula==1):
            reba=8
        elif(rula==2):
            reba=8
        elif(rula==3):
            reba=8
        elif(rula==4):
            reba=9
        elif(rula==5):
            reba=10
        elif(rula==6):
            reba=10
        elif(rula==7):
            reba=10
        elif(rula==8):
            reba=10
        elif(rula==9):
            reba=10
        elif(rula==10):
            reba=11
        elif(rula==11):
            reba=11
        else:
            reba=11
    elif(x==9):
        if(rula==1):
            reba=9
        elif(rula==2):
            reba=9
        elif(rula==3):
            reba=9
        elif(rula==4):
            reba=10
        elif(rula==5):
            reba=10
        elif(rula==6):
            reba=10
        elif(rula==7):
            reba=11
        elif(rula==8):
            reba=11
        elif(rula==9):
            reba=11
        elif(rula==10):
            reba=12
        elif(rula==11):
            reba=12
        else:
            reba=12
    elif(x==10):
        if(rula==1):
            reba=10
        elif(rula==2):
            reba=10
        elif(rula==3):
            reba=10
        elif(rula==4):
            reba=11
        elif(rula==5):
            reba=11
        elif(rula==6):
            reba=11
        elif(rula==7):
            reba=11
        elif(rula==8):
            reba=12
        elif(rula==9):
            reba=12
        elif(rula==10):
            reba=12
        elif(rula==11):
            reba=12
        else:
            reba=12
    elif(x==11):
        if(rula==1):
            reba=11
        elif(rula==2):
            reba=11
        elif(rula==3):
            reba=11
        elif(rula==4):
            reba=11
        elif(rula==5):
            reba=12
        elif(rula==6):
            reba=12
        elif(rula==7):
            reba=12
        elif(rula==8):
            reba=12
        elif(rula==9):
            reba=12
        elif(rula==10):
            reba=12
        elif(rula==11):
            reba=12
        else:
            reba=12
    else:
        reba=12
    if(duration>1):
        reba+=1
        


    
    
    return reba 

mp_drawing.DrawingSpec

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
    
        image = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Make detection
        




        
        
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        

t2= datetime.now()
t3=t2-t1       # create root window
print ((t3.total_seconds())*1000)
cv2.imshow('Mediapipe Feed', image)


cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()


def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 
def calculate_angle2(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = (radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 
for lndmrk in mp_pose.PoseLandmark:
    print(lndmrk)


## Setup mediapipe instance
uarm=0
larm=0
wrist=0
wrist_twist=0
uarm2=0
larm2=0
wrist2=0
wrist_twist2=0
lst=[]

trunk=0
neck=0
trunk2=0
neck2=0
rula=0
reba=0
knee=0
knee2=0

i=1
if(side.get()=="R"):
    with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
    
        try:
            landmarks = results.pose_landmarks.landmark
            
           
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle<=100):
                larm=1
            else:
                larm=2 
            lst.append((i,"RElbow",angle))
            i+=1
            
            
            
            # Visualize angle
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(elbow, [x,y]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA
                                )
           
            shoulder = [landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
             
            lst.append((i,"RTrunk",angle))
            i+=1
            if(angle<1):
                trunk=0
            elif(angle<=20):
                trunk=1
            elif(angle<=60):
                trunk=2
            else:
                trunk=3

            
            
            
            # Visualize angle
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(elbow, [x,y]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA
                                )
            
            
            elbow = [landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y]
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y]
            
            # Calculate angle
            xx=calculate_angle(shoulder, elbow, wrist)
            if(xx<0):
                
                neck=3
            else:
                angle = 180-int(x)
                
                if(angle<=10):
                    neck=1
                elif(angle<=20):
                    neck=2
                else:
                    neck=2
           
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle<=30):
                knee=1
            elif(angle<=60):
                knee=2
            else:
                knee=3 
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            # Calculate angle
            angle2 = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle2>60 and abs(angle-angle2)>30):
                knee+=1

            lst.append((i,"RKnee",angle))
            i+=1
            
            # Visualize angle
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(elbow, [x,y]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            

            

            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle<60 or angle>120):
                larm+=1
            

            
            # Visualize angle
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(elbow, [x,y]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            
            

            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            
            # Visualize angle
            cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            shoulder = [landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle<=20):
                uarm=1
            elif(angle<=45):
                uarm=2
            elif(angle<=90):
                uarm=3
            else:
                uarm=4
            if(int(arm.get())==1):
                uarm=max(uarm-1,1)
            lst.append((i,"RShoulder",angle))
            i+=1
            # Visualize angle
            cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            

            

            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            if(angle<=1):
                wrist=1
            elif(angle<=15):
                wrist=2
            else:
                wrist=3
            lst.append((i,"RWrist",angle))
            i+=1
            
            
            # Visualize angle
            cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y]
            
            # Calculate angle
            angle =180- int(calculate_angle(shoulder, elbow, wrist))
            if(angle<=150):
                wrist+=1
            
            
            # Visualize angle
            
            
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            
            # Calculate angle
            angle = 180-int(calculate_angle(shoulder, elbow, wrist))
            
            # Visualize angle
            cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            
        except:
            pass
        
        wrist_twist=int(twist.get())
        print(wrist,wrist_twist,uarm,larm)
        
        rula=rulaC(uarm,larm,wrist,wrist_twist,int(time.get()),int(load.get()),int(leg.get()),neck,trunk,int(neck_bend.get()),int(neck_twist.get()),int(trunk_bend.get()),int(trunk_twist.get()))  
        reba=rebaC(uarm,larm,wrist,wrist_twist,int(time.get()),int(load.get()),int(leg.get()),neck,trunk,int(neck_bend.get()),int(neck_twist.get()),int(trunk_bend.get()),int(trunk_twist.get()),int(couple.get()),knee)  
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Mediapipe Feed', image)

        cv2.waitKey(0)
else:

    with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as pose:
        
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle<=100):
                    larm2=1
                else:
                    larm2=2 
                lst.append((i,"LElbow",angle))
                i+=1

                
                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [x,y]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA
                                    )
               
                cv2.imshow('Mediapipe Feed', image)
                cv2.waitKey(0)
               
                shoulder = [landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                
                lst.append((i,"LTrunk",angle))
                i+=1
                if(angle<1):
                    trunk2=0
                elif(angle<=20):
                    trunk2=1
                elif(angle<=60):
                    trunk2=2
                else:
                    trunk2=3

                
                
                
                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [x,y]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA
                                    )
                cv2.imshow('Mediapipe Feed', image)
                cv2.waitKey(0)
               
                elbow = [landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y]
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y]
                
                # Calculate angle
                xx=calculate_angle(shoulder, elbow, wrist)
                if(xx<0):
                   
                    neck2=3
                else:
                    angle = 180-int(xx)
                    
                   
                    if(angle<=10):
                        neck2=1
                    elif(angle<=20):
                        neck2=2
                    else:
                        neck2=2
                

                
                
                
                
               
                
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle<=30):
                    knee2=1
                elif(angle<=60):
                    knee2=2
                else:
                    knee2=3 
                shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                
                # Calculate angle
                angle2 = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle2>60 and abs(angle-angle2)>30):
                    knee2+=1
                lst.append((i,"LKnee",angle))
                i+=1
                # Visualize angle
                cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)


                cv2.imshow('Mediapipe Feed', image)
                cv2.waitKey(0)


                
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                
                # Calculate angle
                angle = int(calculate_angle(shoulder, elbow, wrist))
                if(angle<60 or angle>120):
                    larm2+=1 
                

                
                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [x,y]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                
                # Visualize angle
                cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)

               

                shoulder = [landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle<=20):
                    uarm2=1
                elif(angle<=45):
                    uarm2=2
                elif(angle<=90):
                    uarm2=3
                else:
                    uarm2=4
                if(int(arm.get())==1):
                    uarm2=max(uarm2-1,1)
                lst.append((i,"LShoulder",angle))
                i+=1
                
                
                # Visualize angle
                cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)

                
              
                
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle<=150):
                    wrist2+=1
                
                # Visualize angle
                
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                if(angle<=1):
                    wrist2=1
                elif(angle<=15):
                    wrist2=2
                else:
                    wrist2=3
                lst.append((i,"LWrist",angle))
                i+=1
                
                
                # Visualize angle
                cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
                
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                
                # Calculate angle
                angle = 180-int(calculate_angle(shoulder, elbow, wrist))
                
                # Visualize angle
                cv2.putText(image, str(angle), tuple(np.multiply(elbow, [x,y]).astype(int)),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
            except:
                pass
            
            wrist_twist=int(twist.get())
            print(wrist,wrist_twist,uarm,larm)
            rula=rulaC(uarm2,larm2,wrist2,wrist_twist,int(time.get()),int(load.get()),int(leg.get()),neck2,trunk2,int(neck_bend.get()),int(neck_twist.get()),int(trunk_bend.get()),int(trunk_twist.get()))
            reba=rebaC(uarm2,larm2,wrist2,wrist_twist,int(time.get()),int(load.get()),int(leg.get()),neck2,trunk2,int(neck_bend.get()),int(neck_twist.get()),int(trunk_bend.get()),int(trunk_twist.get()),int(couple.get()),knee2)
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            cv2.imshow('Mediapipe Feed', image)

            cv2.waitKey(0)


cv2.destroyAllWindows()
lst.append((i,"Rula",rula))
i+=1
print(lst)
if(rula<=2):

    lst.append((i,"Rula_Result","Safe, no action required"))
elif(rula<=4):
    lst.append((i,"Rula_Result","Low risk, change may needed"))
elif(rula<=6):
    lst.append((i,"Rula_Result","Medium risk, Investigate and change soon"))
else:
    
    lst.append((i,"Rula_Result","High risk, Implement change now"))
i+=1
lst.append((i,"Reba",reba))
i+=1
if(reba<=1):

    lst.append((i,"Reba_Result","Safe"))
elif(reba<=3):
    lst.append((i,"Reba_Result","Low risk, change may needed"))
elif(reba<=7):
    lst.append((i,"Reba_Result","Medium risk, Investigate and change soon"))
elif(reba<=10):
    
    lst.append((i,"Reba_Result","High risk,Investigate and implement change now"))
else:
    lst.append((i,"Reba_Result","Very high risk, Implement change"))

r=len(lst)
print ("Runtime :",(t3.total_seconds())*1000,end="")
print("ms")
root = Tk()
t = Table(root,lst,r)
root.mainloop()

            

