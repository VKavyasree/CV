#Image loading

import cv2
image=cv2.imread("eight.jpg")

#Dimension
if image is not None:
    h,w,c=image.shape
    print(f"Height:{h}\nWidth={w}\nChannels={c}")
else:
    print("Error loading image. Please check the show file path or format.") 

#Image Display and saving on HD
user_input = input("Enter the function to be  performed:\n")
if user_input == "show":
    cv2.imshow("Window",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif user_input == "save":
    cv2.imwrite("saved_image.jpg",image)
else:
    print("Invalid input. Please enter 'show' or 'save'.")


#Image converted from BGR to Grayscale and display
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
if gray is not None:
    cv2.imshow("GrayscaleImage",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error converting image to grayscale.")

#Save the grayscale image
cv2.imwrite("grayscale_image.jpg", gray)