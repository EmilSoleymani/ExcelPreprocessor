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
    if not type(a) == str:
        a = str(a)
    return hashlib.sha256(a.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    data = pd.read_excel('./TestDataCustom.xlsx')
    
    hashCols = []
    delCols = []

    with open('hashColumns.txt', 'r') as f:
        hashCols = f.readlines()
    
    with open('deleteColumns.txt', 'r') as f:
        delCols = f.readlines()

    colNames = data.columns.to_list()

    for col in hashCols:
        colName = col.strip()

        if not colName in colNames:
            print("Warning: Cannot hash non-existant column \"", colName, "\" from data!", sep="")
            continue

        data[col.strip()] = data[col.strip()].apply(getHash)

    for col in delCols:
        colName = col.strip()

        if not colName in colNames:
            print("Warning: Cannot delete non-existant column \"", colName, "\" from data!", sep="")
            continue

        data = data.drop(columns=[colName])

    data.to_excel('./test.xlsx')
