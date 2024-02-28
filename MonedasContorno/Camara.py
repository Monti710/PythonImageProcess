import cv2 as cv
import numpy as np

capturaVideo=cv.VideoCapture(1)
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    tipocamara,camara=capturaVideo.read()
    grises= cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow("Camara Android", grises)
    if cv.waitKey(1)==ord("q"):
        break
capturaVideo.release()
cv.destroyAllWindows()