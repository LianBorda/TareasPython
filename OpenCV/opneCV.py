import cv2 
import numpy as np

kernel = np.ones((5,5), np.uint8)
im = cv2.imread('Leon.jpg')
ims = cv2.resize(im,(500,500))

imgr = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imsr = cv2.resize(imgr,(500,500))

imCanny = cv2.Canny(im, 150, 200)
imcr = cv2.resize(imCanny,(500,500))

imDialation = cv2.dilate(imCanny, kernel, iterations=1)
imcd = cv2.resize(imDialation,(500,500))

imEroded = cv2.erode(imDialation,kernel,iterations=1)
imce = cv2.resize(imEroded,(500,500))

imd=cv2.rectangle(im,(100,900),(500,300),(0,0,255),cv2.FILLED)
imdd = cv2.resize(imd,(500,500))

cv2.imshow("Normal", ims)
cv2.imshow("EscalaGris", imsr)
cv2.imshow("BordeadoCanny", imcr)
cv2.imshow("BordeadoDialation", imcd)
cv2.imshow("BordeadoEroded", imce)
cv2.imshow("NormalConRectángulo", imdd)

cv2.waitKey(0)