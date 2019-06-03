def linemaster(line, lineofline):
	print(f"you have {line} lines!")
	print(f"you have another {lineofline} lineofline )")
	print('why you should have another "line"???')

print("We can print lines directly to print how many of lines.")
linemaster(10,40)

print("or we can use variable from our script.")
amount_of_lines = 40
amount_of_linesofline = 50
linemaster(amount_of_lines,amount_of_linesofline)

print("we can even do math in our fuction calling")
linemaster(10*7,9*2)

print("and we can comine the two, variable and math")
linemaster(amount_of_lines+24, amount_of_linesofline+9)

