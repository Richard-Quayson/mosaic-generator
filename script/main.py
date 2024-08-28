from extract import main as generate_colour_list
from mosaic import Mosaic
import importlib.util
import os


def create_mosaic(colour_list: list[list]) -> None:
    """
    Creates a mosaic using the given colour list

    Args:
        - colour_list (list[list]): the colour list to use for the mosaic

    Returns:
        - None
    """

    mosaic = Mosaic(colour_list=colour_list)
    mosaic.turtle.speed(0)
    mosaic.draw_squares()
    mosaic.turtle.hideturtle()


def main(filepath: str, dimension: int) -> None:
    """
    Generates a mosaic from a PDF file

    Args:
        - filepath (str): the path to the PDF file
        - dimension (int): the dimension of the rubix cube, eg. 3 for 3x3x3, 4 for 4x4x4, etc.
    
    Returns:
        - None
    """
    
    # generate colour list and get the path to the generated Python file and the variable name
    colour_list_path, colour_list_variable = generate_colour_list(file_path=filepath, dimension=dimension)

    # extract the module name from the generated Python file path
    module_name = os.path.splitext(os.path.basename(colour_list_path))[0]

    # dynamically import the module using the generated Python file path
    spec = importlib.util.spec_from_file_location(module_name, colour_list_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # get the dynamically imported variable using its name stored in colour_list_variable
    colour_list = getattr(module, colour_list_variable)

    # generate mosaic using the imported colour list
    create_mosaic(colour_list)

    print("Done generating mosaic 😊!")


if __name__ == "__main__":
    filepath = "../sample_images/rq/rq.pdf"
    dimension = 7
    main(filepath=filepath, dimension=dimension)
