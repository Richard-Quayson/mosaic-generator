"""Mosaic image generator using turtle graphics.

This module generates a mosaic image using turtle graphics. The mosaic image is
composed of a grid of squares, each filled with a colour. The number of rows and
columns in the grid, as well as the colour list, can be specified when creating
an instance of the Mosaic class.

@author:    
Written by Richard Quayson, 2024.
"""

import sys
import os

# adding the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import turtle
import random
from sample_images.m3.m3 import M3_COLOUR_LIST


class Mosaic:
    """Mosaic image generator class.

    Attributes:
        rows (int): The number of rows in the grid.
        columns (int): The number of columns in the grid.
        ROW_HEIGHT (float): The height of each row in the grid.
        COLUMN_WIDTH (float): The width of each column in the grid.
        colour_list (list): A list of colours to fill the squares with.
        turtle (turtle.Turtle): The turtle object used to draw the mosaic.
    """

    # class variables
    window = turtle.Screen()
    WIDTH = window.window_width() / 2
    HEIGHT = window.window_height() - 100
    ROW_HEIGHT = 0  # (will be calculated later)
    COLUMN_WIDTH = 0  # (will be calculated later)
    BORDER_BOTTOM_X = -WIDTH // 2
    BORDER_BOTTOM_Y = HEIGHT // 2 - HEIGHT
    SQUARE_NUM_SIDES = 4

    COLOUR_LIST = [
        "white",
        "yellow",
        "blue",
        "green",
        "red",
        "orange",
    ]  # list of Rubik's cube colours

    COLOUR_DICT = {
        "W": "white",
        "Y": "yellow",
        "B": "#0000E7",
        "G": "#00FF00",
        "R": "#FF0000",
        "O": "#FF9900",
    }

    def __init__(self, num_rows, num_columns, colour_list=None):
        """Initializes a new Mosaic instance.

        Args:
            num_rows (int): The number of rows in the grid.
            num_columns (int): The number of columns in the grid.

        Optional Args:
            colour_list (list): A 2D list of colours to fill the squares with.

        Optional argument colour_list controls the image generated by the mosaic.
        If colour_list is not provided, the squares will be filled with random colours.
        """

        self.rows = num_rows
        self.columns = num_columns
        self.ROW_HEIGHT = Mosaic.HEIGHT / self.rows
        self.COLUMN_WIDTH = Mosaic.WIDTH / self.columns
        self.colour_list = colour_list
        self.turtle = turtle.Turtle()

    def bottom_left_right(self):
        """Positions the turtle at the bottom left corner of the grid."""

        self.turtle.penup()
        self.turtle.goto(
            self.BORDER_BOTTOM_X, self.BORDER_BOTTOM_Y
        )  # bottom left corner
        self.turtle.setheading(0)

    def draw_grid_border(self):
        """Draws the border of the grid."""

        self.turtle.penup()
        self.turtle.goto(-Mosaic.WIDTH // 2, Mosaic.HEIGHT // 2)
        self.turtle.pendown()
        self.turtle.setheading(270)  # set the direction of the turtle to down

        for _ in range(2):
            self.turtle.forward(Mosaic.HEIGHT)
            self.turtle.left(90)
            # temporal fix for more width space
            # need to review the square size computation to resolve it without
            # this manual rescaling
            self.turtle.forward(Mosaic.WIDTH - (3 * (self.WIDTH / self.columns)))
            self.turtle.left(90)

    def draw_row(self, x, y):
        """DEPRECATED/UNUSED IN CURRENT MOSAIC IMAGE GENERATION.

        Draws a horizontal line at the given coordinates.

        Args:
            x (float): The x-coordinate of the starting point.
            y (float): The y-coordinate of the starting point.
        """

        self.bottom_left_right()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.forward(self.WIDTH)  # draw the row using the width of the grid

    def draw_rows(self):
        """DEPRECATED/UNUSED IN CURRENT MOSAIC IMAGE GENERATION.

        Draws the horizontal lines of the grid.
        """

        for i in range(self.rows):
            self.draw_row(
                self.BORDER_BOTTOM_X, self.BORDER_BOTTOM_Y + i * self.ROW_HEIGHT
            )

    def draw_column(self, x, y):
        """DEPRECATED/UNUSED IN CURRENT MOSAIC IMAGE GENERATION.

        Draws a vertical line at the given coordinates.

        Args:
            x (float): The x-coordinate of the starting point.
            y (float): The y-coordinate of the starting point.
        """

        self.bottom_left_right()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.setheading(90)
        self.turtle.forward(self.HEIGHT)

    def draw_columns(self):
        """DEPRECATED/UNUSED IN CURRENT MOSAIC IMAGE GENERATION.

        Draws the vertical lines of the grid.
        """

        for i in range(self.columns):
            self.draw_column(
                self.BORDER_BOTTOM_X + i * self.COLUMN_WIDTH, self.BORDER_BOTTOM_Y
            )

    def draw_square_shape(self):
        """Draws a square shape using the turtle graphics."""

        for _ in range(self.SQUARE_NUM_SIDES):
            self.turtle.right(90)
            self.turtle.forward(self.HEIGHT / self.rows)

    def draw_square(self, x, y, row):
        """Utilises the draw_square_shape method to draw a square in the grid.

        Args:
            x (float): The x-coordinate of the starting point.
            y (float): The y-coordinate of the starting point.
            row (int): The row number of the square.
        """

        self.bottom_left_right()
        for col in range(self.columns):

            # incrementally move to the right per the COLUMN_WIDTH
            self.turtle.goto(x + (self.HEIGHT / self.rows) * (col), y)
            self.turtle.pendown()

            # fill the square with a colour
            if self.colour_list:
                if self.colour_list[row - 1][col] in self.COLOUR_DICT:
                    self.turtle.fillcolor(
                        self.COLOUR_DICT[self.colour_list[row - 1][col]]
                    )
                else:
                    # randomly select a colour from the list if colour at given index is not in colour dict
                    self.turtle.fillcolor(random.choice(self.COLOUR_LIST))
            else:
                # randomly select a colour from the list if colour_list is not provided
                self.turtle.fillcolor(random.choice(self.COLOUR_LIST))

            self.turtle.begin_fill()
            self.turtle.setheading(0)
            self.turtle.forward(self.WIDTH / self.columns)

            # draw the square shape
            self.draw_square_shape()

            self.turtle.end_fill()

    def draw_squares(self):
        """Utilises the draw_square method to draw the squares in the grid."""

        for row in range(1, self.rows + 1):
            self.draw_square(
                self.BORDER_BOTTOM_X, self.BORDER_BOTTOM_Y + row * self.ROW_HEIGHT, row
            )


if __name__ == "__main__":
    mosaic = Mosaic(num_rows=90, num_columns=60, colour_list=M3_COLOUR_LIST)
    mosaic.turtle.speed(0)
    mosaic.draw_grid_border()
    mosaic.draw_squares()
    mosaic.turtle.hideturtle()
    turtle.done()
