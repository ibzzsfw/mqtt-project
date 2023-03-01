import excel_reader as reader

"""
    Test Script for ExcelReader class
"""
filePath = "D:\Project\mqtt-project\input.xlsx"

# Create an object of ExcelReader class
excel_reader = reader.ExcelReader(filePath)

# Read excel file
excel_reader.read_excel()

# Read excel sheet
excel_reader.read_excel_sheet("node1")

# Print excel file
excel_reader.print_excel()

# Print excel sheet
excel_reader.print_excel_sheet("node1")