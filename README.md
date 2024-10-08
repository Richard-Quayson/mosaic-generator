# Mosaic Generator

A Python application that creates a mosaic image using turtle graphics. The program dynamically generates a color list from a PDF file and uses this list to draw a mosaic based on the Rubik's cube dimensions selected by the user.

## Features

- Generates a color list from a PDF file for a mosaic image.
- Utilizes turtle graphics to draw the mosaic.
- Supports custom dimensions for better image quality.

## Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Setup

### Step 1: Set Up a Virtual Environment and Install Dependencies

1. **Create a virtual environment** to manage project dependencies:

   ```bash
   python -m venv mosaic-venv
   ```

2. **Activate the virtual environment**:

   - On Windows:

     ```bash
     mosaic-venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source mosaic-venv/bin/activate
     ```

3. **Install the required dependencies** listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Generate the Mosaic PDF

1. Visit [https://bestsiteever.ru/mosaic/](https://bestsiteever.ru/mosaic/) to generate the PDF file for the color list.
2. Follow the instructions on [this GitHub repository](https://github.com/Roman-/mosaic) to understand how to create the mosaic PDF.
3. **Note**: For better image quality, it is recommended to choose Rubik's cube dimensions of **5 and above**.

### Step 3: Update the Project with Your File Path

1. Once you have generated the PDF file, update the `filepath` and `dimension` variables in the `script/main.py` file to reflect the path where your image is located:

   ```python
   if __name__ == "__main__":
       filepath = "../sample_images/<your_initials>/your_file.pdf"
       dimension = <your_selected_dimension>  # 3 for 3x3x3, 5 for 5x5x5, etc
   ```

2. For a more organized approach, create a directory in `sample_images/<your_initials>/` to store your PDF file.

### Step 4: Run the Program

1. Open your terminal and navigate to the `script` directory:

   ```bash
   cd script
   ```

2. Run the following command to execute the program and create your mosaic image:

   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
