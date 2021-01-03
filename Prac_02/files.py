# 1

name = input("What is our name?  ")
OUT_FILE = "name.txt"
file_out = open(OUT_FILE, 'w')
print(name, file=file_out)
file_out.close()

# 2
file_in = open(OUT_FILE, 'r')
name = file_in.read().strip()
print("Your name is {}".format(name))
file_in.close()

# 3
in_file = open("number.txt", 'w')
integer1 = 17
integer2 = 42
integer3 = 400
in_file.write('17\n')
in_file.write('42\n')
in_file.write('400\n')
in_file.close()
in_file = open("number.txt", 'r')
total = integer1 + integer2
print(total)
in_file.close()

# 4
in_file = open("number.txt", 'r')
total = integer1 + integer2 + integer3

print(total)
