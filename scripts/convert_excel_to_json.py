import pandas as pd
import json
import os

# Define input and output paths
base_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_dir, "../data")
output_folder = os.path.join(base_dir, "../output")
excel_file = "example.xlsx"
sheet_name = "sheet_name"
output_file = "output.json"

# Full file paths
input_path = os.path.abspath(os.path.join(input_folder, excel_file))
output_path = os.path.abspath(os.path.join(output_folder, output_file))

try:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Output folder created at: {output_folder}")

    # Read the Excel file
    print(f"Reading Excel file: {input_path}")
    df = pd.read_excel(input_path, sheet_name=sheet_name, engine="openpyxl", dtype=str)
    
    # Clean whitespace
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert to JSON
    print("Converting data to JSON format...")
    json_data = df.to_dict(orient="records")

    # Write to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print(f"JSON file successfully created at: {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")
