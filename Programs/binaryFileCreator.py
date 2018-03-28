#This program creates a txt file that contains the training data for the Neural Network(NN).
#The data is a random binary number and the neurone that should fire.
#The variable nbBin represent the number of binary characters you want your binary number to
#have. This is the only variable you have to modify to change the output in your file,
#anything else is asked when you run the program.
#The format of the file is important for the good function of the NN so please don't alter it.
#The output file has the total number of training cycles as first line and then starts the training
#data : first the binary form of the number and then the representation of the correct neurone that
#should fire (represented by the 1, and 0 representing a neurone that shouldn't fire). This representation
#has 2^nbBin numbers
#Example : I have the decimal number 7 with a nbBin = 4
#My first line of data would be 0111 (the binary form of the decimal 7, with 4 binary slots)
#The second line would be 0000000100000000 (the 1 is on the 8th slot on 16, representing the decimal nb 7)
#			  (0123456789111111)(these lines are not in the file, they just name the different slots)
#			  ( 	     012345)
#This repeats the number of times you want, which is asked inside the program.


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
			a = a + str(round(random.random()))		#Creates a random binary number to solve
		
		F.write(a)
		F.write('\n')
		dec = int(a,2)						#Creates the decimal version of the binary number
		
		for i in range(pow(2,nbBin)):				#Creates a string of 2^nbBin digits that show to the Neural
			if i == dec: 					#Network the correct neurone to fire on the final layer.
				F.write('1')				#The string has the same nb of chars as the final layer has
			else:						#neurones. The 1 represents the neurone that should have fired,
				F.write('0')				#the 0 shows that the neurone shouldn't have fired.
				
		F.write('\n')
		a = ''
	F.close()

if __name__ == '__main__':
	main()
