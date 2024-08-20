import cv2
import os

def extract_objects(segmented_image_path, output_folder):
    if not os.path.isfile(segmented_image_path):
        raise FileNotFoundError(f"Segmented image not found: {segmented_image_path}")

    # Load the segmented image
    segmented_image = cv2.imread(segmented_image_path, cv2.IMREAD_GRAYSCALE)
    if segmented_image is None:
        raise ValueError(f"Failed to load image: {segmented_image_path}")

    # Threshold the image to get binary mask
    _, binary_mask = cv2.threshold(segmented_image, 1, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        object_image = segmented_image[y:y+h, x:x+w]
        object_image_path = os.path.join(output_folder, f'object_{i}.png')
        cv2.imwrite(object_image_path, object_image)
        print(f"Saved object {i} to {object_image_path}")

if __name__ == "__main__":
    import sys
    segmented_image_path = sys.argv[1]
    output_folder = sys.argv[2]
    os.makedirs(output_folder, exist_ok=True)
    extract_objects(segmented_image_path, output_folder)
