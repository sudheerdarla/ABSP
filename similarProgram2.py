

# --------------------------- Clean up dates in different date formats ---------------------


date = "13-11-2017 asf 2014.07.20 14/07/2071 2015.6.15 asdf 01-2017-15"
dateRegex = re.compile('(\d{1,4})[/.-](\d{1,4})[/.-](\d{1,4})')
match = dateRegex.findall(date)
years = []
months = []
days = []

for i in range(len(match)):
	for j in range(len(match[i])):
		if len(str(match[i][j])) > 2:  # for years
			years.append(match[i][j])
		if 1 <= int(match[i][j]) < 12:  # for months
			months.append(match[i][j])
		if 1 <= int(match[i][j]) < 31:  # for days
			days.append(match[i][j])

for i in range(len(match)):
	print(days[i] + '/' + months[i] + '/' + years[i] )


