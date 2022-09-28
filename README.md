# Excel Preprocess

Given Excel file `TestDataCustom.xlsx` (name hard-coded for now), hashes all values in columns specified in `hashColumns.txt` (also hard-coded for now) and deletes all columns specified in `deleteColumns.txt` (also hard-coded for now). Exports to file `test.xlsx` (also hard-coded for now).

## Build

Execute `make build` to install required packages.

## Run

Execute `make` to execute script.

## Tests

Ran this script on test data in `TestDataCustom.xlsx` and got the output in `test.xlsx`.
