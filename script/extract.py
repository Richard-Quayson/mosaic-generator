import fitz

FIRST_QUADRANT = "A1"
MIN_NUM_SUB_QUADRANTS_PER_ROW = 2
MAX_NUM_SUB_QUADRANTS_PER_ROW = 3
BLOCK_WITH_MIN_SUB_QUADRANTS = "G"
BLOCK_LETTER_INDEX = 0
BLOCK_NUMBER_INDEX = 1


def extract_text(filepath: str):
    """
    Extracts text from a PDF file
    
    Args:
        - filepath (str): the path to the PDF file
    
    Returns:
        - str: the text extracted from the PDF file
    """

    # open the PDF file
    pdf_document = fitz.open(filepath)
    
    # extract text from each page
    extracted_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        extracted_text += page.get_text()

    # write extracted text to a file
    output_filepath = filepath.replace(".pdf", ".txt")
    with open(output_filepath, "w") as output_file:
        output_file.write(extracted_text)

    return extracted_text


def create_row_colour_list(sub_quadrant_one: list, sub_quadrant_two: list, sub_quadrant_three: list, current_block_letter: str, block_list: list) -> list[list]:
    """
    Creates a row colour list from the sub quadrants

    Args:
        - sub_quadrant_one (list): the first sub quadrant
        - sub_quadrant_two (list): the second sub quadrant
        - sub_quadrant_three (list): the third sub quadrant
        - current_block_letter (str): the current block letter
        - block_list (list): the current block list

    Returns:
        - list: colour list for the rows in the block list
    """

    # reverse the quadrant items
    sub_quadrant_one = sub_quadrant_one[::-1]
    sub_quadrant_two = sub_quadrant_two[::-1]
    sub_quadrant_three = sub_quadrant_three[::-1]

    for row_num in range(len(sub_quadrant_one)):
        row = list()
        row.extend(sub_quadrant_one[row_num])
        row.extend(sub_quadrant_two[row_num])
        
        if current_block_letter != BLOCK_WITH_MIN_SUB_QUADRANTS:
            row.extend(sub_quadrant_three[row_num])
                                
        if row_num < len(block_list):
            current_row_list = block_list[row_num]
        else:
            current_row_list = list()
            block_list.append(current_row_list)
        
        current_row_list.extend(row)
        block_list[row_num] = current_row_list
    
    return block_list


def extract_colour_list(extracted_text: str, dimension: int = 3):
    """
    Extracts the colour list from the extracted text

    Args:
        - extracted_text (str): the text extracted from the PDF file
        - dimension (int): the dimension of the rubix cube, eg. 3x3x3, 4x4x4, etc.
    
    Returns:
        - list: the colour list extracted from the text

    NOTE:
        - A block is a collection of rows
        - A row is a collection of sub quadrants
    """

    colour_list = list()

    block_list = list()
    current_block_letter = None
    current_block_number = None

    sub_quadrant_one = list()
    sub_quadrant_two = list()
    sub_quadrant_three = list()

    start = False
    MIN_NUM_SUB_QUADRANT_ITEMS_PER_ROW = dimension * MIN_NUM_SUB_QUADRANTS_PER_ROW
    MAX_NUM_SUB_QUADRANT_ITEMS_PER_ROW = dimension * MAX_NUM_SUB_QUADRANTS_PER_ROW

    for line in extracted_text.split("\n"):
        if not start:
            start = line.startswith(FIRST_QUADRANT)
            
            if start:
                line_content = line.strip()
                current_block_letter = line_content[BLOCK_LETTER_INDEX]
                current_block_number = line_content[BLOCK_NUMBER_INDEX]
                quadrant_line_count = 0 # keep track of the number of lines read per quadrant 
        else:
            line_content = line.strip().split()

            if len(line_content) == 1:
                # new block begins after this line
                block_letter = line_content[0][BLOCK_LETTER_INDEX]
                block_number = line_content[0][BLOCK_NUMBER_INDEX]

                # if the block letter changes, add the current sub quadrants to the block list
                if block_letter != current_block_letter:
                    # create the block list
                    block_list = create_row_colour_list(sub_quadrant_one, sub_quadrant_two, sub_quadrant_three, current_block_letter, block_list)
                    current_block_letter = block_letter

                    # empty the sub quadrants
                    quadrant_line_count = 0

                    sub_quadrant_one = list()
                    sub_quadrant_two = list()
                    sub_quadrant_three = list()

                # if the block number changes, append the block list to the colour list
                if block_number != current_block_number:
                    current_block_number = block_number
                    
                    # add block list to the colour list
                    colour_list.extend(block_list)

                    # empty the block list
                    block_list = list()

            else:
                if current_block_letter.upper() == BLOCK_WITH_MIN_SUB_QUADRANTS:
                    if (quadrant_line_count % MIN_NUM_SUB_QUADRANT_ITEMS_PER_ROW) < (dimension):
                        sub_quadrant_one.append(line_content)
                    else:
                        sub_quadrant_two.append(line_content)

                else:
                    if (quadrant_line_count % MAX_NUM_SUB_QUADRANT_ITEMS_PER_ROW) < (dimension):
                        sub_quadrant_one.append(line_content)
                    elif (quadrant_line_count % MAX_NUM_SUB_QUADRANT_ITEMS_PER_ROW) < (2 * dimension):
                        sub_quadrant_two.append(line_content)
                    else:
                        sub_quadrant_three.append(line_content)
                
                quadrant_line_count += 1
        
    # remove last list if it is empty
    if len(sub_quadrant_one[-1]) == 0:
        sub_quadrant_one.pop()
    if len(sub_quadrant_two[-1]) == 0:
        sub_quadrant_two.pop()
    
    # add the last block to the colour list
    block_list = create_row_colour_list(sub_quadrant_one, sub_quadrant_two, sub_quadrant_three, current_block_letter, block_list)

    colour_list.extend(block_list)
    return colour_list


def create_colour_list_file(colour_list: list, file_path: str):
    """
    Creates a colour list file from the extracted colour list

    Args:
        - colour_list (list): the extracted colour list
        - file_path (str): the path to the PDF file

    Returns:
        - None 
    """

    output_filepath = file_path.replace(".pdf", ".py")
    variable_name = file_path.split("/")[-1].replace(".pdf", "").upper() + "_COLOUR_LIST"

    # create the colour list file which will have a variable equal to the colour list
    with open(output_filepath, "w") as output_file:
        output_file.write(f"{variable_name} = [\n")
        for row_num in range(len(colour_list)):
            output_file.write(f"    # ROW: {row_num + 1}\n") 
            output_file.write(f"    {colour_list[row_num]},\n")
        output_file.write("]\n")
    
    print(f"Colour list file created at {output_filepath}")


if __name__ == "__main__":
    file_path = "sample_images/rq/rq.pdf"
    extracted_text = extract_text("sample_images/rq/rq.pdf")
    colour_list = extract_colour_list(extracted_text, 7)
    create_colour_list_file(colour_list, file_path)