import cv2 
import numpy as np

codigo = np.ones((5,5), np.uint8)
im = cv2.imread('Espacio.jpg')
ims = cv2.resize(im,(450,450))

imgr = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imsr = cv2.resize(imgr,(450,450))

imCanny = cv2.Canny(im, 150, 200)
imcr = cv2.resize(imCanny,(450,450))

imDialation = cv2.dilate(imCanny, codigo, iterations=1)
imcd = cv2.resize(imDialation,(450,450))

imEroded = cv2.erode(imDialation,codigo,iterations=1)
imce = cv2.resize(imEroded,(450,450))

imd=cv2.rectangle(im,(150,300),(400,400),(0,0,255), cv2.FILLED)
imdd = cv2.resize(imd,(450,450))

cv2.imshow("Normal", ims)
cv2.imshow("EscalaGris", imsr)
cv2.imshow("Canny", imcr)
cv2.imshow("Dialation", imcd)
cv2.imshow("Eroded", imce)
cv2.imshow("Rectángulo", imdd)

cv2.waitKey(0)
#

