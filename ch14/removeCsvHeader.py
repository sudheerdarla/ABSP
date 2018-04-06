#! python3
# removeCsvHeader.py - Removes the header from all CSV files 
# in the current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('csv'):
		continue	# skip non-csv files

	print('Removing header from ' + csvFilename + '...')

	# Read the CSV file in (skipping first row).
	csvRows = []
	file = open(csvFilename)
	fileReader = csv.reader(file)
	for row in fileReader:
		if fileReader.line_num == 1:
			continue # skip first row
		csvRows.append(row)
	file.close()

	# Write out the CSV file
	csvFile = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
	csvWriter = csv.writer(csvFile)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFile.close()
