
# coding: utf-8


#Importing the required libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt


#convert to img rgb format
img = cv2.imread("image.png",1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#different colors are detected by visiting 20 * 25 squares on the picture 
x = 5
y = 0
color_group = 0 
colors = []
colors_II=[]
colors.append([0,0,0])
color = [255,255,255]
state  = "new_color"
while (x<350):
    while (y< 350):
        y = y+25
        img_crop = img[x:x+24,y:y+24]
        if img_crop[12,12][0] != 232 :
            color[0]= img_crop[12,12][0]
            color[1]= img_crop[12,12][1]
            color[2]= img_crop[12,12][2]
            for i in colors:
                if i[0] == color[0] and i[1] == color[1] and i[2] == color[2]:

                    state = " same color"
                    break
                else:
                    
                    state = "new color"
            if state == "new color":
                print "new color detected! RGB value -->  " + str(img_crop[12,12]) 
                colors.append(img_crop[12,12])
                colors_II.append(img_crop)
                plt.imshow(img_crop)
                plt.show()
    x=x+25
    y = 0
print colors



# Separate masking for detected colors
color_group =  len(colors_II)
masks = []
hsv_frame = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
for i in colors_II:
    x = cv2.cvtColor(i,cv2.COLOR_RGB2HSV)
    hsv_value = x[12,12]
    lowwer = x[12,12]
    upper = x[12,12]
    lowwer[0] = lowwer[0]-10 
    upper[0] = upper[0] + 10
    mask = cv2.inRange(hsv_frame,lowwer,upper)
    masks.append(mask)
    plt.imshow(mask)
    plt.show()



# Dilate function is used for a whole
kernel = np.ones((5,5),np.uint8)
finals = []
for i in masks:
    x = cv2.dilate(i,kernel,iterations = 1)
    finals.append(x)
    plt.imshow(x)
    plt.show()



# Detecting the number of images in pictures
cnt_number = []
for i in finals:
    plt.imshow(i)
    plt.show()
    f, contours,h = cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x =len(contours)
    cnt_number.append(x)
    print x
    



# Results are printed on the screen
plt.imshow(img)
plt.show()
print "number of color detected: " + str(color_group)
print "blue --> " + str(cnt_number[0])
print "red --> " + str(cnt_number[1])
print "green --> " + str(cnt_number[2])
print "orange --> " + str(cnt_number[3])

