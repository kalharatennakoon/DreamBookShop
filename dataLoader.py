# pip install pandas matplotlib numpy seaborn adjustText openpyxl

# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# load the dataset
class DataLoader:
    def load(self, file_path="Dataset_Books.csv"):
        try:
            # Check if file path is provided and not empty
            if not file_path:
                print("Error: No file path provided.")
                return None
            
            # If running from tests directory, adjust path
            if not os.path.exists(file_path) and os.path.exists(f"../{file_path}"):
                file_path = f"../{file_path}"
                
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' not found.")
                return None
            
            # Try to read CSV and validate it has proper structure
            df = pd.read_csv(file_path)
            
            # Check if DataFrame is empty or has no proper columns
            if df.empty:
                print(f"Error: File '{file_path}' is empty.")
                return None
                
            if len(df.columns) == 0:
                print(f"Error: Invalid CSV format in '{file_path}' - no columns found.")
                return None
                
            return df
            
        except pd.errors.EmptyDataError:
            print(f"Error: File '{file_path}' is empty or has invalid CSV format.")
            return None
        except pd.errors.ParserError:
            print(f"Error: File '{file_path}' has invalid CSV format or structure.")
            return None
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error loading file '{file_path}': {e}")
            return None


