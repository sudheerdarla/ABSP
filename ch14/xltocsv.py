#! python3

# xltocsv.py - Loop through every .xlsx file copy data from another
# .CSV files with the filename of excel_sheet.csv format.

import csv, openpyxl, os


for excelFile in os.listdir('.'):
	# Skip non-xlsx files, load the workbook object.
	if excelFile.endswith('.xlsx'):
		wb = openpyxl.load_workbook(excelFile)
		for sheetName in wb.sheetnames:
			sheet = wb[sheetName]
			# Create the CSV filename from the Excel file name and
			# sheet title.
			csvFile = os.path.splitext(os.path.basename(excelFile))[0] + '_' + sheetName + '.csv'
			# Create the csv.writer object for this CSV file.
			csvOutFile = open(csvFile, 'w', newline='')
			csvOutWriter = csv.writer(csvOutFile)

			# Loop through every row in a sheet.
			for rowNum in range(1, sheet.max_row + 1):
				rowData = []
				# Loop through each cell in the row.
				for colNum in range(1, sheet.max_column + 1):
					rowData.append(sheet.cell(row=rowNum, column=colNum).value)

				csvOutWriter.writerow(rowData)

			csvOutFile.close()
