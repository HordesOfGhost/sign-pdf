----
# sign-pdf

This application allows you to sign PDF documents with an image of your signature.

## Prerequisites

Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your system.

## Installation

1. **Create a Conda Environment**

   ```sh
   conda create --name sign-pdf python=3.8
   ```

2. **Activate the Environment**

   ```sh
   conda activate sign-pdf
   ```

3. **Install Dependencies**

   Make sure you have a `requirements.txt` file in the root directory of your project. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

To sign a PDF, run the following command:

```sh
python app.py --pdf path/to/your_pdf.pdf --sign path/to/your_sign(.jpg/.png) --output path/to/your_signed_pdf.pdf
```

### Command Line Arguments

- `--pdf`: Path to the PDF file that you want to sign.
- `--sign`: Path to the image file of your signature.
- `--output`: Path where the signed PDF will be saved.

## Example

Here's an example command to sign a PDF:

```sh
python app.py --pdf documents/sample.pdf --sign images/signature.png --output signed_documents/signed_sample.pdf
```

## Usage Instructions

After running the application, a window will appear allowing you to draw the rectangular area where the signature will be placed. Follow these steps:

1. Draw the rectangular sign area.
2. Press `a` to add the signature after each rectangular box drawn
3. Press `s` to save the signed PDF.
4. If you need to retry, press `r`.

![Drawing Rectangular Sign Area](Screenshot%20(117).png)

