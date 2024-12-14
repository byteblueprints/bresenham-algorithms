import cv2
import numpy as np

from bresenham import get_bresenhams_line
from xiaolin_wu_line import xiaolin_wu_line

# Generate the line coordinates using the get_bresenhams_line function
line_coord = get_bresenhams_line(250, 20, 450, 450)

# Create a white image of size 500x500
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Iterate over the generated line coordinates
for coord in line_coord:
    x, y = coord[0], coord[1]

    # Ensure the coordinates are within image bounds
    if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
        # Set the pixel color to black for the current coordinate
        image[y, x] = (0, 0, 0)

        # Display the image with the current line pixel colored
        cv2.imshow('Breshenham Algorithm', image)
        cv2.waitKey(10)

# Close all OpenCV windows
cv2.destroyAllWindows()

line_pixels = xiaolin_wu_line(250, 20, 450, 450)

# Create a white image of size 500x500
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Iterate over the generated line pixels
for pixel in line_pixels:
    x, y, intensity = pixel
    grayscale_value = int((1 - intensity) * 255)  # Convert intensity to grayscale (0-255)

    # Ensure the coordinates are within image bounds
    if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
        image[y, x] = (grayscale_value, grayscale_value, grayscale_value)  # Set pixel intensity

        # Display the image with the current line pixel colored
        cv2.imshow('Xiaolin Wu Line', image)
        cv2.waitKey(10)

# Close all OpenCV windows
cv2.destroyAllWindows()
