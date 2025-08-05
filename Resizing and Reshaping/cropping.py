import cv2
image=cv2.imread("eight.jpg")

if image is not None:
    cropped_image=image[200:700,50:700]

if cropped_image is not None:

    cv2.imshow("Original image",image)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 