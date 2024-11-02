import json

def extract_code_cells(ipynb_file_path):
    # Open and read the notebook file
    with open(ipynb_file_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    # Extract the code from code cells
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code = ''.join(cell['source'])
            code_cells.append(code)

    return code_cells

def main():
    # Path to your notebook file in Google Drive
    ipynb_file_path = './upload_docs.ipynb'

    code_cells = extract_code_cells(ipynb_file_path)

    # Print the extracted code
    for i, code in enumerate(code_cells, start=1):
        print(f"Code Cell {i}:\n{code}\n{'='*40}\n")

if __name__ == '__main__':
    main()
