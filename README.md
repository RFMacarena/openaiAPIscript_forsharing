# Clinical Data Extractor using OpenAI API

## Description
This Python project automates the extraction of structured information from clinical reports using OpenAI's GPT models. It includes two python files: `openai_api_calls.py` and `main_script.py`.

- `openai_api_calls.py`: Handles API calls to OpenAI's GPT models, containing the `clinical_data_extractor` function to generate responses based on clinical data.

- `main_script.py`: Processes a set of clinical reports from an Excel file and extracts structured information. It uses the `clinical_data_extractor` for generating query prompts and also includes a `get_estimated_cost` function for token usage cost estimation.

## Prerequisites
- Python 3.x
- OpenAI Python package
- pandas
- tiktoken
- openpyxl

## Installation
1. Clone the repository:
```python
git clone https://github.com/RFMacarena/openaiAPIscript_forsharing.git
```
2. Install the required packages:
```python
pip install openai pandas tiktoken openpyxl
```

## Usage
To process a batch of clinical reports, execute the main function in main_script.py. This function reads an API key from a text file, processes a specified number of patient reports from an Excel file, and uses a specified model and query type for data extraction.
```python
def main():
 api_file = "openai_key.txt"
 with open(api_file, 'r') as file:
     api_key = file.read().strip()

 file_path = './data/Dataset_AP.xlsx'
 num_pacientes = 5
 model = "gpt-3.5-turbo-1106"  # Could be "gpt-3.5-turbo-1106" or "gpt-4-1106-preview"
 query_type = "AP"  # Extracting comorbidities and lifestyle risk factors from personal history reports
 extract_data_from_reports(api_key, file_path, num_pacientes, model, query_type)
```

## License
MIT License