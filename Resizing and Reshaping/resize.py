import cv2 
image=cv2.imread("eight.jpg")

#here in resize function the dimension of the image to be resized is in format (width,height)
new_resized=cv2.resize(image,(300,300))
if new_resized is not None:
    cv2.imshow("Resized image",new_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()