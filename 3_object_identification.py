import os
import torch
from torchvision import transforms
from PIL import Image
#
# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def identify_objects(objects_dir):
    # Loop over all images in the objects directory
    for filename in os.listdir(objects_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(objects_dir, filename)
            
            # Load image and perform inference
            image = Image.open(image_path).convert("RGB")
            results = model(image)
            
            # Save results
            results.save(save_dir=objects_dir)  # Save the results back to the directory

            print(f"Identified and saved results for {filename}")

if __name__ == "__main__":
    import sys
    objects_dir = sys.argv[1]
    os.makedirs(objects_dir, exist_ok=True)
    identify_objects(objects_dir)
