"""
This script is used for anonymizing student data requried to run
the SortingHat program. This data is needed for testing.

Author: Emil Soleymani
Date: Sep 28, 2022
"""

import hashlib
import pandas as pd

def getHash(a: str) -> str:
    """
    Returns hash of input string `a`. Uses `sha256` hashing algorithm.
    """

    # Make sure type of data is str
    if not type(a) == str:
        a = str(a)
    return hashlib.sha256(a.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    data = pd.read_excel('./TestDataCustom.xlsx')
    
    hashCols = []
    delCols = []

    # Read columns to hash
    with open('hashColumns.txt', 'r') as f:
        hashCols = f.readlines()
    
    # Read columns to delete
    with open('deleteColumns.txt', 'r') as f:
        delCols = f.readlines()

    # Names of all valid columns
    colNames = data.columns.to_list()

    # For all specified columns to hash
    for col in hashCols:
        # Remove newline at end of line (or possible empty spaces)
        colName = col.strip()

        # If column doesn't exist
        if not colName in colNames:
            # Print warning and go to next column to hash
            print("Warning: Cannot hash non-existant column \"", colName, "\" from data!", sep="")
            continue
        
        # Hash all values in a column
        data[colName] = data[colName].apply(getHash)

    # For all specified columns to delete
    for col in delCols:
        # Remove newline newline at end of line (or possible empty spaces)
        colName = col.strip()

        # If column doesn't exist
        if not colName in colNames:
            # Print warning and go to next column to delete
            print("Warning: Cannot delete non-existant column \"", colName, "\" from data!", sep="")
            continue
        
        # Drop column
        data = data.drop(columns=[colName])

    # Write to file
    data.to_excel('./test.xlsx')
