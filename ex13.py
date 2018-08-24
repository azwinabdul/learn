from sys import argv

script, first, second, third = argv


print("the script is called:", script)
print("your first variable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)

data = input("input your data here ")
print(f"""data your inputed is "{data}" it's right??""")


x = int(input("masukan angka pertama mu di sini :"))
y = int(input("masukan angka kedua di sini :"))
xy = x + y
print(f"jadi angka {x} ditambah {y} hasilnya {xy}")

x1 = input("masukan angka di sini :")
x2 = input("masukan angka kedua di sini")
xx = x1 + x2
print(f"""jadi angka {x1} kalau ditambah {x2} jadinya {xx} karena dia bukan integer tapi string 
	gabisa di print biasa ok???""")