import openpyxl

wb1 = openpyxl.load_workbook('example.xlsx')
sheet1 = wb1['Sheet1']

wb2 = openpyxl.load_workbook('censuspopdata.xlsx')
sheet2 = wb2['Population by Census Tract']

if sheet1['A3'].value != sheet2['A3'].value:
	print('nope!')