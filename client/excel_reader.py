import pandas as pd

class ExcelReader:

        # Constructor to initialize file path
        def __init__(self, file_path):
            self.file_path = file_path

        # Function to read excel file, return dataframe
        def read_excel(self):
            df = pd.read_excel(self.file_path)
            return df

        # Function to read excel file, return dictionary
        def read_excel_dict(self):
            df = pd.read_excel(self.file_path)
            return df.to_dict()
        
        # Function to read excel sheet, return dataframe
        def read_excel_sheet(self, sheet_name):
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            return df
        
        # Function to read excel sheet, return dictionary
        def read_excel_sheet_dict(self, sheet_name):
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            return df.to_dict()
        
        # Function to print excel file
        def print_excel(self):
            print(self.read_excel())

        # Function to print excel sheet
        def print_excel_sheet(self, sheet_name):
            print(self.read_excel_sheet(sheet_name))
