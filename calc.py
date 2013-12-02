# идеальный вес - 45 кг на первые 150 см роста + на каждый сантиметр по кг+10 % разброс

name = input("What is your name? ")
growth = input("What is your growth (cm)?  ")
weight=0
if int(growth)<150: 
	print(name+", your ideal weight - 45 kilogramms")
else:
	sr=(int(growth)-150)+45
	min=sr-sr%10
	max=sr+sr%10
	mess=name+", your ideal weight is range from "+str(min)+" to "+str(max)
	print(mess)
	