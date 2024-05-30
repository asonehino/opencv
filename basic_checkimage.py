import cv2 as cv
import sys



#변수 저장
img = cv.imread("./basic/image.jpg")

#파일이 없을 경우 경고 메시지
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)

#s를 누르면 image2로 저장
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("image2.jpg", img)