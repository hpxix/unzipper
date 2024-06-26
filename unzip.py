import zipfile
import os

def unzip_file(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    zip_file = os.path.join(current_directory, "stocks-main.zip")  # Replace with your zip file name
    
    try:
        unzip_file(zip_file)
        print(f"Successfully extracted files from {zip_file}")
    except Exception as e:
        print(f"Failed to extract files: {e}")
