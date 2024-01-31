from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    """
    Extracts text from a given image using OCR.

    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None


if __name__ == "__main__":
    # Replace 'path/to/image.png' with the actual path to your test image
    image_path = 'example/images/sample_1.png'
    extracted_text = extract_text_from_image(image_path)
    print(f"Extracted Text:\n{extracted_text}")
