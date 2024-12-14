# Bresenham's Line Algorithm

This repository contains an implementation of Bresenham's Line Algorithm in Python. The algorithm is used to calculate a list of pixel coordinates that form a line between two points on a 2D grid. It is highly efficient and commonly used in computer graphics for rendering straight lines on raster displays.

## Overview

Bresenham's Line Algorithm is an efficient method for drawing lines between two points on a pixel grid. This implementation handles horizontal, vertical, diagonal, and sloped lines with any given start and end points.

## Function: `get_bresenhams_line`

### Description:
`get_bresenhams_line(x0, y0, x1, y1)` generates a list of pixel coordinates that lie on a straight line between two points `(x0, y0)` and `(x1, y1)`.

### Parameters:
- `x0 (int)`: The x-coordinate of the starting point.
- `y0 (int)`: The y-coordinate of the starting point.
- `x1 (int)`: The x-coordinate of the ending point.
- `y1 (int)`: The y-coordinate of the ending point.

### Returns:
- `list of tuple`: A list of pixel coordinates that lie on the line connecting `(x0, y0)` and `(x1, y1)`.

### How it works:
The algorithm determines the slope of the line between the start and end points and uses different strategies for different types of lines:
- **Horizontal or Vertical Lines**: If either the horizontal or vertical distance (`dx` or `dy`) is 0, it uses simple iteration along one axis.
- **Diagonal Lines**: For lines with a slope of 1 (45-degree diagonal), the algorithm handles both x and y increments simultaneously.
- **Other Slopes**: For lines with slopes greater or less than 1, the algorithm adjusts based on the slope to minimize pixel calculations.

### Example Usage:
```python
from bresenham import get_bresenhams_line

# Define starting and ending points
x0, y0 = 10, 20
x1, y1 = 50, 80

# Generate line coordinates
line = get_bresenhams_line(x0, y0, x1, y1)

# Output the list of coordinates
print(line)
```

# Xiaolin Wu's Line Algorithm

This repository contains an implementation of Xiaolin Wu's Line Algorithm in Python. The algorithm is used to calculate a list of pixel coordinates with intensity values to form an anti-aliased line between two points on a 2D grid. It is widely used in computer graphics for rendering smooth lines on raster displays.

## Overview

Xiaolin Wu's Line Algorithm is an efficient method for drawing anti-aliased lines between two points on a pixel grid. Unlike traditional line-drawing algorithms like Bresenham's, this algorithm assigns intensity values to pixels based on their proximity to the ideal line, resulting in smoother and visually appealing lines.

## Function: `xiaolin_wu_line`

### Description:
`xiaolin_wu_line(x0, y0, x1, y1)` generates a list of pixel coordinates along with their intensity values that form a smooth line between two points `(x0, y0)` and `(x1, y1)`.

### Parameters:
- `x0 (float)`: The x-coordinate of the starting point.
- `y0 (float)`: The y-coordinate of the starting point.
- `x1 (float)`: The x-coordinate of the ending point.
- `y1 (float)`: The y-coordinate of the ending point.

### Returns:
- `list of tuple`: A list of tuples, where each tuple contains:
  - `x (int)`: The x-coordinate of the pixel.
  - `y (int)`: The y-coordinate of the pixel.
  - `i (float)`: The intensity value of the pixel (ranges from 0 to 1).

### How it works:
- **Anti-Aliasing**: The algorithm calculates fractional intensities for pixels near the line to minimize the jagged appearance.
- **Steep Lines**: For lines with a steep slope, the roles of x and y are swapped to ensure proper handling.
- **Endpoints**: The algorithm handles endpoints separately for precision.
- **Line Traversal**: Pixels along the line are calculated using incremental updates based on the line's slope.

### Example Usage:
```python
from xiaolin_wu_line import xiaolin_wu_line

# Define starting and ending points
x0, y0 = 10, 20
x1, y1 = 50, 80

# Generate line coordinates with intensities
line = xiaolin_wu_line(x0, y0, x1, y1)

# Output the list of coordinates with intensities
for pixel in line:
    print(f"Pixel: ({pixel[0]}, {pixel[1]}), Intensity: {pixel[2]:.2f}")
```