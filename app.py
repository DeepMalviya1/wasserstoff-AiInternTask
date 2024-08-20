import streamlit as st
import subprocess
import os
import json

# Title of the Streamlit app
st.title("AI Pipeline for Image Segmentation and Object Analysis ")

# Create necessary directories if they don't exist
os.makedirs("data/input_images", exist_ok=True)
os.makedirs("data/segmented_objects", exist_ok=True)
os.makedirs("data/output", exist_ok=True)

# Image upload section
st.header("1. Upload Your Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image_path = f"data/input_images/uploaded_image.{uploaded_file.name.split('.')[-1]}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(image_path, caption='Uploaded Image', use_column_width=True)
    
    # Run the pipeline
    st.header("2. Processing Pipeline")
    with st.spinner('Processing...'):
        try:
            # Run each step of the pipeline
            subprocess.run(["python", "1_image_segmentation.py", image_path, "data/segmented_objects/segmented_image.png"], check=True)
            st.success("Step 1: Image Segmentation Complete")
            
            subprocess.run(["python", "2_object_extraction.py", "data/segmented_objects/segmented_image.png", "data/segmented_objects/"], check=True)
            st.success("Step 2: Object Extraction Complete")
            
            subprocess.run(["python", "3_object_identification.py", "data/segmented_objects/"], check=True)
            st.success("Step 3: Object Identification Complete")
            
            subprocess.run(["python", "4_text_extraction.py", "data/segmented_objects/"], check=True)
            st.success("Step 4: Text Extraction Complete")
            
            subprocess.run(["python", "5_summarize_attributes.py", "data/segmented_objects/"], check=True)
            st.success("Step 5: Summary Attributes Complete")
            
            subprocess.run(["python", "6_data_mapping.py", "data/segmented_objects/"], check=True)
            st.success("Step 6: Data Mapping Complete")
            
            subprocess.run(["python", "7_generate_output.py", image_path, "data/output/mapped_data.json"], check=True)
            st.success("Step 7: Final Output Generation Complete")
            
            # Display image comparison
            st.header("3. Image Comparison")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(image_path, caption='Original Image', use_column_width=True)
            with col2:
                obj_img_path = "data/segmented_objects/object_0.png"
                if os.path.exists(obj_img_path):
                    st.image(obj_img_path, caption='Extracted Object', use_column_width=True)
                else:
                    st.write("Extracted object image not found.")
            with col3:
                st.image("data/segmented_objects/segmented_image.png", caption='Segmented Image', use_column_width=True)
            
            # Display processed object images
            st.header("4. Processed Objects")
            for filename in os.listdir("data/segmented_objects/"):
                if filename.endswith(".png") or filename.endswith(".jpg"):
                    st.image(os.path.join("data/segmented_objects/", filename), caption=filename, use_column_width=True)
            
            # Display JSON data
            st.header("5. Mapped Data")
            mapped_data_path = "data/output/mapped_data.json"
            if os.path.exists(mapped_data_path):
                with open(mapped_data_path, "r") as f:
                    mapped_data = json.load(f)
                st.json(mapped_data)

            # Process Complete Tab
            st.header("6. Process Complete")
            st.success("All processing steps are complete! Check the results above for detailed outputs.")
            # Copyright notice
            st.markdown("---")
            st.markdown("© 2024 Deep Malviya. All rights reserved.")
        except subprocess.CalledProcessError as e:
            st.error(f"Pipeline step failed: {e}")
