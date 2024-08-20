import os
import json
import matplotlib.pyplot as plt
import cv2

def generate_output(input_image_path, mapped_data_path):
    with open(mapped_data_path, "r") as f:
        mapped_data = json.load(f)

    img = cv2.imread(input_image_path)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    for object_name, data in mapped_data.items():
        plt.text(10, 30, f"{data['object_id']}: {data['description']}", color='white')

    plt.axis('off')
    output_image_path = "data/output/final_output.png"
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    plt.savefig(output_image_path)

    # Display the final image and data
    print(f"Final output generated and saved as {output_image_path}")

if __name__ == "__main__":
    import sys
    input_image_path = sys.argv[1]
    mapped_data_path = sys.argv[2]
    os.makedirs("data/output", exist_ok=True)
    generate_output(input_image_path, mapped_data_path)
