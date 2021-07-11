import cv2

import pyautogui
import np


trained_cars_data = cv2.CascadeClassifier('cars.xml')

img = cv2.imread('face3.png')


#viedo = cv2.VideoCapture('Video.mp4')
camera = cv2.VideoCapture('video2.mp4')
while True:
    
    screen = pyautogui.screenshot()
    screen2 = np.array(screen)
    screen2 = screen2[:, :, ::-1].copy()
    grayscaled_img = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_cars_data.detectMultiScale(grayscaled_img)
    for i in range(len(face_coordinates)):
        x , y, w , h = face_coordinates[i]
        cv2.rectangle(screen2,  (x, y), (x+w, y+h), (0,255,0),3,0)



    cv2.imshow('Widzisz mnie??',screen2)

    key = cv2.waitKey(1)
    #jesli q to wyjdz
    if key==81 or key==113:
        cv2.destroyAllWindows()
        break
cv2.waitKey()

print("Working!")