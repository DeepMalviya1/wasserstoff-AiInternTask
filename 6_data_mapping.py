import os
import json

def map_data(input_folder):
    mapped_data = {}
    summary_path = "data/output/summary_attributes.json"
    
    with open(summary_path, "r") as summary_file:
        summary = json.load(summary_file)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            mapped_data[filename] = summary[filename]

    mapped_data_path = "data/output/mapped_data.json"
    os.makedirs(os.path.dirname(mapped_data_path), exist_ok=True)
    with open(mapped_data_path, "w") as mapped_file:
        json.dump(mapped_data, mapped_file, indent=4)

if __name__ == "__main__":
    import sys
    input_folder = sys.argv[1]
    os.makedirs("data/output", exist_ok=True)
    map_data(input_folder)
