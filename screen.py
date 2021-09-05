import cv2
from random import randrange
import pyautogui
import np

#wytrenowanie modelu
trained_face_data = cv2.CascadeClassifier('faces.xml')
trained_eyes_data = cv2.CascadeClassifier('eyes.xml')

#załadowanie zdjęcia/filmu/kamerki
img = cv2.imread('face3.png')


#viedo = cv2.VideoCapture('Video.mp4')
camera = cv2.VideoCapture('video2.mp4')
while True:
    
    screen = pyautogui.screenshot()
    screen2 = np.array(screen)
    screen2 = screen2[:, :, ::-1].copy()
    grayscaled_img = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    eyes_coordinates = trained_eyes_data.detectMultiScale(grayscaled_img)


    for i in range(len(face_coordinates)):
        x , y, w , h = face_coordinates[i]
        cv2.rectangle(screen2,  (x, y), (x+w, y+h), (0,255,0),3,0)
    if len(face_coordinates)>0:

        for i in range(len(eyes_coordinates)):
            x , y, w , h = eyes_coordinates[i]
            
            screen2 = cv2.rectangle(screen2,  (x, y), (x+w, y+h), (255,0,0),3,0)
            cv2.putText(screen2, 'oko', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
            #print("eye detected") 

    cv2.imshow('Widzisz mnie??',screen2)

    key = cv2.waitKey(1)
    #jesli q to wyjdz
    if key==81 or key==113:
        cv2.destroyAllWindows()
        break



"""while True:

    successful_screen2_read, screen2 = camera.read()
    #zamiana na czarno-białe
    grayscaled_img = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)
    


    #wykrywanie twarzy o różnych rozmiarach 
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    eyes_coordinates = trained_eyes_data.detectMultiScale(grayscaled_img)

    #rysowanie ramki 
    print(face_coordinates)
    #dla kazdej twarzy na zdjęciu
    for i in range(len(face_coordinates)):
        x , y, w , h = face_coordinates[i]
        cv2.rectangle(screen2,  (x, y), (x+w, y+h), (0,255,0),3,0) #randrange(128,256), randrange(256), randrange(256)
    #to samo dla oczu
    for i in range(len(eyes_coordinates)):
        x , y, w , h = eyes_coordinates[i]
        cv2.rectangle(screen2,  (x, y), (x+w, y+h), (255,0,0),3,0)
        print("eye detected")





    #czeka milisekunde na klawisz 
    cv2.imshow('Widzisz mnie??',screen2)
    key = cv2.waitKey(1)
    #jesli q to wyjdz
    if key==81 or key==113:
        break
    #jesli p to zatrzymaj 
    if key==112:
        while True:
            key = cv2.waitKey(1)
            if key == 112:
                break
camera.relase()"""
"""
#zamiana na czarno-białe
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#wykrywanie twarzy o różnych rozmiarach 
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


#rysowanie ramki 
print(face_coordinates)
#dla kazdej twarzy na zdjęciu
for i in range(len(face_coordinates)):
    x , y, w , h = face_coordinates[i]
    cv2.rectangle(img,  (x, y), (x+w, y+h), (randrange(128,256), randrange(256), randrange(256)),3,0)


#wyswietlenie okeinka
cv2.imshow('Widzisz mnie??',img)"""

cv2.waitKey()

print("Working!")