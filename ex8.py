formatter = "{} {} {} {}"
a = 'durian'
b = 'kelapa'
c = 'apel'
d = 'kedongdong'


print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try Your",
	"Own text here",
	"Maybe a poem",
	"Or anything you like or a song about fear."
))
print(formatter.format(a, b, c, d))