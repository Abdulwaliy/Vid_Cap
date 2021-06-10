

import time
import cv2
import numpy as np
import os

# Enter the file name
user_input = int(input('Enter image file number                    '))

# Set interval to save recurring image files
time_count = 10

# Save image file name  to local memory
user_input = os.path.join(os.getcwd(), str(user_input))
print("ALl logs saved in dir:", user_input)
os.mkdir(user_input)

# Saving recurring image files to local memory
image_file_count = 1
image_file = os.path.join(user_input, str(image_file_count) + ".png")
print("Capture image saved location : {}".format(image_file))

#initiate time
start = time.time()

#initiate video capture
v = cv2.VideoCapture(0)
v.set(cv2.CAP_PROP_FRAME_WIDTH,640)
v.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

# face classifier
face_cascade = cv2.CascadeClassifier('opencv_algorithm\data\haarcascade_frontalface_alt2.xml')

# face capture and save operation
while(True):
    ret, frame = v.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,  5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi = gray[y:y+h, x:x+w]
        image='image_item.png'
        if time.time() - start > time_count:
            start = time.time()
            image_file_count += 1
            b= cv2.imwrite(image_file, roi)
            image_file = os.path.join(user_input, str(image_file_count) + ".png")
            b= cv2.imwrite(image_file, roi)
            colour=(255,0,0)
            stroke = 2
            cv2.rectangle(frame, (x,y), (x+w ,y+h),colour,stroke) #width, height
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
            break
v.release()
cv2.destroyAllWindows()





