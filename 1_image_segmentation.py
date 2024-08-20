import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.models.segmentation import deeplabv3_resnet101
import numpy as np
import matplotlib.pyplot as plt
import os

def segment_image(image_path, output_path):
    model = deeplabv3_resnet101(pretrained=True)
    model.eval()
    
    input_image = Image.open(image_path).convert("RGB")
    preprocess = T.Compose([
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)['out'][0]
    
    output_predictions = output.argmax(0)
    output_predictions = output_predictions.byte().cpu().numpy()

    plt.imshow(output_predictions)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    import sys
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    segment_image(input_image_path, output_image_path)
