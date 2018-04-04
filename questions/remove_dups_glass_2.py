filename = input("Enter path to file") or "./dups.txt"

my_file = open(filename)
hash_table = {}

for line in my_file:
	hash_table[line] = 1

for key in hash_table.keys():
	print(key)
