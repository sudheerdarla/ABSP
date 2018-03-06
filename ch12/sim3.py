import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

for rows in sheet['A1' : 'C' + str(sheet.max_row)]:
	for cell in rows:
		if cell.value == None:
			print(':( - ' + cell.coordinate + ' is empty')
		else: 
			print(':)')