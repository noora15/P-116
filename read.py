import cv2

# Read Image
img = cv2.imread("solar-system.jpg")

cv2.putText(img, 'sun', (20,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'mercury', (100,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'venus', (200,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'earth', (300,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'mars', (400,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'jupiter', (550,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'saturn', (750,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'uranus', (950,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(img, 'neptune', (1100,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))

cv2.imshow("output", img)
cv2.waitKey(0)