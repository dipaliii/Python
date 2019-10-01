print("@@@@@@@@@@@ Right Triangle @@@@@@@@@@@")
for i in range(10):
	for j in range(i):
		print("*",end="")
	print("\n")
print("@@@@@@@@@@@ square @@@@@@@@@@@")
for x in range(10):
	for y in range(10):
		print("*",end="")
	print("\n")
print("@@@@@@@@@@@ Pyramid @@@@@@@@@@@")
k = 0
rows = 10
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
