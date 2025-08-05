import cv2
image=cv2.imread("eight.jpg")

flipped=cv2.flip(image,1)
cv2.imshow("Flipped Horizontally:",flipped)
cv2.waitKey(0)

flipped=cv2.flip(image,0)
cv2.imshow("FLipped Vertically:",flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()