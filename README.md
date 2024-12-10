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
