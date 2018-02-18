import random

def main():
	nbLine = int(input('Please enter the number of numbers you want: '))
	nbBin = 3
	a = ''
	
	printBin(nbLine, nbBin, a)

def printBin(nbLine, nbBin, a):
	fileName = input('Please enter the name of the file you want to create: ')
	F = open(fileName,'w')
	
	F.write(str(nbLine))
	F.write('\n')
	
	for i in range(nbLine):
		for j in range(nbBin):
			a = a + str(round(random.random()))
		
		F.write(a)
		F.write('\n')
		dec = int(a,2)
		
		if(dec == 0):
			F.write('10000000')
			F.write('\n')
		elif(dec == 1):
			F.write('01000000')
			F.write('\n')
		elif(dec == 2):
			F.write('00100000')
			F.write('\n')
		elif(dec == 3):
			F.write('00010000')
			F.write('\n')
		elif(dec == 4):
			F.write('00001000')
			F.write('\n')
		elif(dec == 5):
			F.write('00000100')
			F.write('\n')
		elif(dec == 6):
			F.write('00000010')
			F.write('\n')
		elif(dec == 7):
			F.write('00000001')
			F.write('\n')
		
		a = ''
	F.close()

if __name__ == '__main__':
	main()
