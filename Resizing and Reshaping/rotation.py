import cv2
image=cv2.imread("eight.jpg")

h,w=image.shape[:2]
center=(w//2,h//2)

image1=image[200:700,50:600]

M=cv2.getRotationMatrix2D(center,90,1.0)
rotated=cv2.warpAffine(image1,M,(w,h))

cv2.imshow("Original Image:",image)
cv2.imshow("Rotated image",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()