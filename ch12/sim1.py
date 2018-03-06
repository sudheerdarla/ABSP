import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

data = {}

for rows in range(1, sheet.max_row):
	data[sheet['B' + str(rows)].value] = sheet['C' + str(rows)].value

if data['Apples'] != data['Bananas']:
	print('nope!')