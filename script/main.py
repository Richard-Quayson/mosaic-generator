from extract import main as generate_colour_list
from mosaic import Mosaic


def create_mosaic(colour_list: list[list]) -> None:
    mosaic = Mosaic(colour_list=colour_list)
    mosaic.turtle.speed(0)
    mosaic.draw_squares()
    mosaic.turtle.hideturtle()
    mosaic.turtle.done()


def main(filepath: str) -> None:
    # generate colour list
    colour_list = generate_colour_list(file_path=filepath)

    # generate mosaic
    create_mosaic(colour_list)

    print("Done generating mosaic😊!")
