# Excel to JSON Converter

## Project Description
This project converts an **Excel file (.xlsx)** into a structured **JSON format**.  
It includes:
- A sample Excel file (`example.xlsx`) for demonstration.
- Logic to clean up whitespace and preserve leading zeros in numeric fields.

## Features
- Converts Excel files (`.xlsx`) into JSON format.
- Cleans leading/trailing whitespaces in data.
- Preserves leading zeros (e.g., `"0001"` stays as `"0001"`).
- Includes a sample file (`example.xlsx`) for easy testing.

## Prerequisites
- Python 3.8 or higher
- `pandas` library
- `openpyxl` library

You can install the required libraries using the following command:
```sh
pip install -r requirements.txt
```

## Project Structure

```plaintext
excel-to-json/
│
├── data/                    # Input Excel files
│   └── example.xlsx         # Sample input file
│
├── output/                  # JSON output folder
│   └── output.json          # Generated JSON file
│
├── scripts/                 # Conversion script
│   └── convert_excel_to_json.py
│
├── requirements.txt         # Python dependencies
│
└── README.md                # Documentation
```

## Run with Your Own Excel File

To use your own Excel file:

1. Place your Excel file in the `data/` folder.
   - For example: `data/myfile.xlsx`.

2. Update the script settings:
   - Open `scripts/convert_excel_to_json.py` and modify the following variables:
     ```python
     excel_file = "myfile.xlsx"    # Replace with your Excel file name
     sheet_name = "Sheet1"         # Replace with your sheet name
     output_file = "output.json"   # Specify the output file name
     ```

3. Run the script:
   ```sh
   python scripts/convert_excel_to_json.py
   ```

The generated JSON file will appear in the `output/` folder.