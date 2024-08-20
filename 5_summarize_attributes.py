import os
import json

def summarize_attributes(input_folder):
    summary = {}
    extracted_text_path = "data/output/extracted_text.txt"
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            summary[filename] = {
                "object_id": filename.split(".")[0],
                "description": f"Object in {filename}",
                "text": extract_text_from_file(extracted_text_path, filename)
            }

    summary_path = "data/output/summary_attributes.json"
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    with open(summary_path, "w") as summary_file:
        json.dump(summary, summary_file, indent=4)

def extract_text_from_file(file_path, object_name):
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if object_name in line:
                return lines[i + 1].strip()
    return ""

if __name__ == "__main__":
    import sys
    input_folder = sys.argv[1]
    os.makedirs("data/output", exist_ok=True)
    summarize_attributes(input_folder)
