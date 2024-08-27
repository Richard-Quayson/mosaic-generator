from extract import main as generate_colour_list
from mosaic import Mosaic


def create_mosaic(colour_list: list[list]) -> None:
    mosaic = Mosaic(colour_list=colour_list)
    mosaic.turtle.speed(0)
    mosaic.draw_squares()
    mosaic.turtle.hideturtle()
    mosaic.turtle.done()


def main(filepath: str, dimension: int) -> None:
    # generate colour list
    colour_list = generate_colour_list(file_path=filepath, dimension=dimension)

    # generate mosaic
    create_mosaic(colour_list)

    print("Done generating mosaic😊!")


if __name__ == "__main__":
    filepath = "sample_images/rq/rq.pdf"
    dimension = 7
    main(filepath=filepath, dimension=dimension)
