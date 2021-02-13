import cv2 # Importing the OpenCV module.
from tkinter import filedialog # Importing the tkinter filedialog to let the User select Image File of their Choice.

a = filedialog.askopenfilename(title="Select Image") # Letting the User Choose the Image.
b = cv2.imread(a) # Making the OpenCV read that Image.
c = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY) # Converting that Image to Grayscale.
d = 255 - c # Inverting its Colors.
e = cv2.GaussianBlur(d, (21, 21), 0) # Blurring it using GaussianBlur of OpenCV.
f = 255 - e # Inverting it Back again.
g = cv2.divide(c, f, scale= 255.0) # Making OpenCV differentiate between those Images.

cv2.imshow("Original Image", b) # Displaying the Orginal Image to the User for Comparision Purposes.
cv2.imshow("Image with Filter", g) # Showing the User that Image.
cv2.waitKey(0) # Waiting for the Key 0 to be Pressed.
cv2.destroyAllWindows() # Making OpenCV destroy all windows once key 0 is pressed.