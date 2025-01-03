import facerecognition
import cv2
import numpy as np
import csv
from datetime import datetime
video_capture = cv2.VideoCapture(0)
#load known faces
zoya_image = facerecognition.face_locations("faces/zoya.jpg ")
zoya_encoding = facerecognition.face_encoding(zoya_image)[0]

zara_image =  facerecognition.load_image_file("faces/zara.jpg")
zara_encoding = facerecognition.face_encoding(zara_image)[0]

known_face_encodings = [zoya_encoding,zara_encoding]
known_faces_names = ["zoya","zara"]

#list of expected students 
students = known_faces_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%H:%M:%S")
f = open (f"{current_date}.csv","w+",newline ="")

lnwriter = csv.writer(f)
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BAYER_BG2BGR)
    #recognize faces 
    face_locations = facerecognition.face_locations(rgb_small_frame)

    for face_encoding in face_encodings:
        matches = facerecognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = facerecognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)



        if(matches[best_match_index]):
            name = known_faces_names[best_match_index]



    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break










