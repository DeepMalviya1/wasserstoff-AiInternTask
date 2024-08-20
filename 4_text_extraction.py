import pytesseract
from PIL import Image
import os

def extract_text(input_folder):
    output_file = "data/output/extracted_text.txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as text_file:
        for filename in os.listdir(input_folder):
            if filename.endswith(".png"):
                img_path = os.path.join(input_folder, filename)
                image = Image.open(img_path)
                text = pytesseract.image_to_string(image)
                
                text_file.write(f"Text from {filename}:\n{text}\n\n")

if __name__ == "__main__":
    import sys
    input_folder = sys.argv[1]
    os.makedirs("data/output", exist_ok=True)
    extract_text(input_folder)
