import os
import pandas as pd
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:06:10 2025

@author: User
"""

def Extraccion_datos(excel_path):
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    total_path = current_directory + "\\" + excel_path
    df = pd.read_excel(total_path, sheet_name=0)
    
    # Print the current directory
    print("The current location of the file is:", total_path) 

    
    print(df)
    return df

# def elements(df):
#     for index, row in df.iterrows():
#         print(f"Row {index}: First element = {row[0]}, Fourth element = {row[3]}")
#         input("Press Enter to continue...")  # Wait for user to press Enter


def elements(df):
    for index, row in df.iterrows():
        # Clean the first column (remove blank lines)
        cleaned_value = '\n'.join([line for line in row[0].split('\n') if line.strip()])
        print(f"Row {index}:")
        print(cleaned_value)
        
        cleaned_first = '\n'.join([line for line in row[1].split('\n') if line.strip()])
        print(f"Row {index} - First element (Column3):")
        print(cleaned_first)       
        
        cleaned_second = '\n'.join([line for line in row[2].split('\n') if line.strip()])
        print(f"Row {index} - Second element (Column3):")
        print(cleaned_second)
        
        cleaned_third = '\n'.join([line for line in row[3].split('\n') if line.strip()])
        print(f"Row {index} - Third element (Column3):")
        print(cleaned_third)
        
        cleaned_fourth = '\n'.join([line for line in row[4].split('\n') if line.strip()])
        print(f"Row {index} - Fourth element (Column3):")
        print(cleaned_fourth)
        
        input("Press Enter to continue...")  # Wait for user to press Enter



df = Extraccion_datos("Pruebas_Resultados.xlsx")
elements(df)

