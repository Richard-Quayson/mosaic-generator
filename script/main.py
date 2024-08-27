from mosaic import Mosaic


def create_mosaic(colour_list: list[list]) -> None:
    mosaic = Mosaic(colour_list=colour_list)
    mosaic.turtle.speed(0)
    mosaic.draw_squares()
    mosaic.turtle.hideturtle()
    mosaic.turtle.done()
