import cv2
from random import randrange


#wytrenowanie modelu
trained_face_data = cv2.CascadeClassifier('faces.xml')
#załadowanie zdjęcia
img = cv2.imread('face3.png')
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
cv2.imshow('Widzisz mnie??',img)

cv2.waitKey()

print("Working!")