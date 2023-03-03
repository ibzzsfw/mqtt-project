import pandas as pd

class ExcelReader:

        # Constructor to initialize file path
        def __init__(self, file_path):
            self.file_path = file_path

        # Function to read excel file, return dataframe
        def readExcel(self, sheetName, columnName):
            if (sheetName): self.dataframe = pd.read_excel(self.file_path, sheet_name=sheetName)
            else: self.dataframe = pd.read_excel(self.file_path)

            if (columnName): self.dataframe = self.dataframe[columnName]
            return self.dataframe

        """
        - Print functions
        - Getter and Setter functions
        """
        # Function to print excel file
        def printDataframe(self):
            if (self.dataframe is None):
                print("Dataframe is empty")
            else: print(self.dataframe)

        # Function to get dataframe
        def getDataframe(self):
            if (self.dataframe is None):
                print("Dataframe is empty")
            else: return self.dataframe
        
        # Function to get dataframe as dictionary
        def getDict(self):
            if (self.dataframe is None):
                print("Dataframe is empty")
            else: return self.dataframe.to_dict()
            
        # Function to get file path
        def getFilePath(self):
            return self.file_path
        
        # Function to set file path
        def setFilePath(self, file_path):
            self.file_path = file_path