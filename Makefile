all: run

build:
	pip install pandas openpyxl xlsxwriter xlrd

run: 
	python3 ExcelHash.py