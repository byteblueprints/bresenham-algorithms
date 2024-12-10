import cv2
import numpy as np

from main import get_bresenhams_line

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
        cv2.imshow('Coloring Pixels', image)
        cv2.waitKey(10)

# Close all OpenCV windows
cv2.destroyAllWindows()
