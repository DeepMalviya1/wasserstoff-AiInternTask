# AI Pipeline for Image Segmentation and Object Analysis

## Overview

This project implements an AI pipeline for image segmentation and object analysis. It uses various Python scripts to perform tasks including image segmentation, object extraction, object identification, text extraction, attribute summarization, data mapping, and final output generation. The pipeline is integrated with a Streamlit app for a user-friendly interface.

## Project Structure

The project is organized into the following scripts:

1. **`1_image_segmentation.py`**: Segments images into different objects and saves them.
2. **`2_object_extraction.py`**: Extracts individual objects from segmented images and saves them.
3. **`3_object_identification.py`**: Identifies objects within the extracted images using YOLOv5 and saves the results.
4. **`4_text_extraction.py`**: Extracts text from objects and saves it to a file.
5. **`5_summarize_attributes.py`**: Summarizes object attributes and creates a summary JSON file.
6. **`6_data_mapping.py`**: Maps data based on the summary and saves it to a JSON file.
7. **`7_generate_output.py`**: Generates the final output image with annotations.

The Streamlit app file is named `app.py` and provides a web interface for uploading images, running the pipeline, and viewing results.

## Requirements

To run this project, install the necessary Python packages. Use the following `requirements.txt` to install the dependencies:

**`streamlit==1.23.1`**
**`numpy==1.24.2`**
**`Pillow==9.5.0`**
**`matplotlib==3.7.1`**
**`opencv-python-headless==4.8.0.76`**
**`torch==2.0.1`**
**`torchvision==0.15.1`**
**`yolov5==6.2.7`**

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

1. **Create a Virtual Environment (optional but recommended):**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

1. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt

1. **Run the Streamlit App:**:
   ```bash
   streamlit run app.py
   `
## Usage
**1. Upload Your Image: Use the file uploader in the Streamlit app to upload an image.**

**2. Processing Pipeline: The app will process the image through various stages, including segmentation, object extraction, identification, text extraction, summarization, and data mapping.**

**3. Image Comparison: Compare the original image with the extracted object and segmented image using a slider.**

**4. Processed Objects: View processed objects and their details.**

**5. Mapped Data: Check the JSON data with summarized information.**

## Notes

Ensure that all required directories (data/input_images, data/segmented_objects, data/output) are created as needed by the app.

If you encounter issues with package versions or compatibility, adjust the versions in requirements.txt accordingly.

## UI Snapshots

### 1. Upload Your Image
![Upload Your Image](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/1.png?raw=true)

![Uploaded Image](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/1_1.png?raw=true)

### 2. Processing Pipeline
![Processing Pipeline](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/2.png?raw=true)
### 3. Image Comparison
![Image Comparison](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/3.png?raw=true)

### 4. Processed Objects
![Processed Objects](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/4.png?raw=true)

### 5. Mapped Data
![Mapped Data](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/5.png?raw=true)

### 6. Process Complete
![Process Complete](https://github.com/DeepMalviya1/wasserstoff-AiInternTask/blob/main/UI%20Images/6.png?raw=true)

## Contact
For any questions or issues, please contact:

Name: Deep Malviya

Email: deepmalviya.aie@gmail.com
