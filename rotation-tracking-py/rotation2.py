## the global degrees variable holds the angle rotation value to send to the ESP32


import cv2 as cv
from math import atan2, cos, sin, sqrt, pi
import numpy as np
 

degrees = 0

def drawAxis(img, p_, q_, color, scale):
  p = list(p_)
  q = list(q_)
 
  ## [visualization1]
  angle = atan2(p[1] - q[1], p[0] - q[0]) # angle in radians
  hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
 
  # Here we lengthen the arrow by a factor of scale
  q[0] = p[0] - scale * hypotenuse * cos(angle)
  q[1] = p[1] - scale * hypotenuse * sin(angle)
  cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
 
  # create the arrow hooks
  p[0] = q[0] + 9 * cos(angle + pi / 4)
  p[1] = q[1] + 9 * sin(angle + pi / 4)
  cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
 
  p[0] = q[0] + 9 * cos(angle - pi / 4)
  p[1] = q[1] + 9 * sin(angle - pi / 4)
  cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
  ## [visualization1]
 
def getOrientation(pts, img):
  ## [pca]
  # Construct a buffer used by the pca analysis
  global degrees
  sz = len(pts)
  data_pts = np.empty((sz, 2), dtype=np.float64)
  for i in range(data_pts.shape[0]):
    data_pts[i,0] = pts[i,0,0]
    data_pts[i,1] = pts[i,0,1]
 
# Perform PCA analysis
  mean = np.empty((0))
  mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
 
  # Store the center of the object
  cntr = (int(mean[0,0]), int(mean[0,1]))
  ## [pca]
 
  ## [visualization]
  # Draw the principal components
  cv.circle(img, cntr, 3, (255, 0, 255), 2)
  p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
  p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])
  drawAxis(img, cntr, p1, (255, 255, 0), 1)
  drawAxis(img, cntr, p2, (0, 0, 255), 5)
 
  angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
  ## [visualization]
  degrees = str(-int(np.rad2deg(angle)))
  # Label with the rotation angle
  label = "  Rotation Angle: " + degrees + " degrees"
  textbox = cv.rectangle(img, (cntr[0], cntr[1]-25), (cntr[0] + 250, cntr[1] + 10), (255,255,255), -1)
  cv.putText(img, label, (cntr[0], cntr[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
 
  return angle
 
# Load the image

def begin():
  img = cv.imread("Image.jpg")
  img = cv.resize(img,(927,696))
  
  # Was the image there?
  if img is None:
    print("Error: File not found")
    exit(0)
  
  cv.imshow('Input Image', img)
  
  # Convert image to grayscale
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  # Convert image to binary
  _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
  
  # Find all the contours in the thresholded image
  contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
  
  for i, c in enumerate(contours):
  
    # Calculate the area of each contour
    area = cv.contourArea(c)
  
    # Ignore contours that are too small or too large
    if area < 3700 or 100000 < area:
      continue
  
    # Draw each contour only for visualisation purposes
    cv.drawContours(img, contours, i, (0, 0, 255), 2)
  
    # Find the orientation of each shape
    getOrientation(c, img)


  # Save the output image to the current directory
  #cv.imwrite("outputimg9.jpg", img)  

cap = cv.VideoCapture(0)

# Initialize variables to store the previous position of the detected rectangle
prev_rect_position = None

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help with edge detection
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection to find edges in the frame
    edges = cv.Canny(blurred, 50, 150)

    # Find contours in the edged frame
    contours, _ = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.04 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)

        # Check if the polygon has four vertices (a rectangle)
        if len(approx) == 4 and cv.contourArea(approx) > 1000:
            # Get the bounding box of the rectangle
            x, y, w, h = cv.boundingRect(approx)

            # Calculate the center of the rectangle
            rect_center = (x + w // 2, y + h // 2)

            # Print a message if the rectangle has stopped moving
            if prev_rect_position is not None and np.linalg.norm(np.array(rect_center) - np.array(prev_rect_position)) < 5:
                print("Rectangle has stopped moving!")

                cv.imwrite("Image.jpg", frame)
                begin()

            # Update the previous position
            prev_rect_position = rect_center

    # Display the original frame
    cv.imshow('Object Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# Release the camera and close all OpenCV windows
cap.release()
cv.destroyAllWindows()

