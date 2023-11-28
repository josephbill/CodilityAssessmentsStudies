import math

def polysum(n, s):
    """
    Calculate the sum of the area and square of the perimeter of a regular polygon.

    :param n: Number of sides of the polygon.
    :param s: Length of each side of the polygon.
    :return: The sum of the area and square of the perimeter, rounded to 4 decimal places.
    """
    # Calculate the area of the regular polygon
    area = (0.25 * n * s**2) / math.tan(math.pi / n)

    # Calculate the perimeter of the regular polygon
    perimeter = n * s

    # Calculate the sum of the area and square of the perimeter
    result = area + perimeter**2

    # Round the result to 4 decimal places
    return round(result, 4)


n_sides = 5
side_length = 5
result = polysum(n_sides, side_length)
print(result)