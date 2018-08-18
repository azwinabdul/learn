days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"


data_element = "fire\nwater\nearth\nair"
data_people = "rudi meadow kilmander rakowtas"

formatter ="{} {}"
print("Here are the Days: ", days)
print("Here are the Months", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like. 
Even 4 lines if we want, or 5, or 6
or 7 line like this.
what is not yet 7 lines?
now is 7 lines. """)

print(formatter.format(data_element, data_people))