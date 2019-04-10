from sys import argv

script, filename = argv

txt = open(filename, 'r+')

print(f"File yang kamu buka adalah {filename}")
print(txt.read())

print("Masukan baris baru")
line = input("baris : ")
txt.write(line)
txt.write("\n")

print(txt.read())