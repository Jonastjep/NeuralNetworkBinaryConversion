import neuralLib as nl

def main():
	
	############ VAR AND MATRIX SETUP (you can tweak the variables here) ###############
	title = '3-8-8 with .5 LearningRate' #title of the graph
	nbNeur = [3,8,8]
	nbLay = 3
	LearningRate = .5
	testFile = 'Test_File_NN.txt'		#Filename of the file containing training samples
	
	W = nl.scalableWeightMatrix(nbLay, nbNeur)
	A = nl.vector_A_Matrix(nbLay, nbNeur)
	B = nl.vector_Z_B_Err_Matrix(nbLay, nbNeur, 1.)
	Z = nl.vector_Z_B_Err_Matrix(nbLay, nbNeur, 0.)
	Err = nl.vector_Z_B_Err_Matrix(nbLay, nbNeur, 0.)
	
	################# MAIN LOOP #####################
	Fi = open(testFile,'r')						#File with TestData (binary input) created with binaryFileCreator.py
	
	nbTests = int(Fi.readline().rstrip())		#Imports the number you chose with binaryFileCreator.py as the number of 
												#loops and binary numbers your program will go through (you can change it manually of course)
	
	CostFile = open('CostFile.txt', 'w')		#File where values of cost function are printed
	AnswerFile = open('AnswerFile.txt', 'w')	#File where the output and supposed output can be compared
	
	for m in range(nbTests):
		
		############### FILLS THE INPUT LAYER OF NN ################
		inputVal = Fi.readline().rstrip()
		for i in range(len(A[0])):
			A[0][i] = float(inputVal[i])
			
		waitedNb = int(inputVal, 2)
		
		############### CREATES THE Y VECTOR OF WANTED VALUES ################
		Y = nl.vector_Y_intended(nbLay, nbNeur, y = Fi.readline().rstrip())
		
		############### FEEDFORWARD ################
		nl.feedforward(nbLay,nbNeur,W,B,A,Z)
		
		###################### COMPUTES ERROR OF THE OUTPUT LAYER ################
		Cx = nl.errorL(A,Y,Z,Err, nbLay, nbNeur) #Returns the cost function of the individual test
		
		CostFile.write(str(Cx))
		CostFile.write('\n')
		
		############# MAKES A FILE THAT COMPARES REAL OUTPUT WITH SUPPOSED OUTPUT ##############
		nl.AnswerFilePrintToTxt(A, AnswerFile, waitedNb, nbLay)
		
		############################## BACKPROPAGATES THE ERROR ###########################################
		nl.backpropError(W,A,Y,Z,Err, nbLay, nbNeur)
		
		############################## CREATES THE GRADIENT VECTOR #########################################
		gradient = nl.gradientOutput(Err, A, nbNeur, nbLay)
		
		##################### APPLIES GRADIENT DESCENT TO WEIGHT AND BIAS #######################
		nl.gradientDescent(W,B,gradient,LearningRate, nbNeur, nbLay)
		
	##### CLOSES THE TEXT FILES #####
	Fi.close()
	CostFile.close()
	AnswerFile.close()
	
	######### CREATES THE PLOT OF THE COST FUCTION AT EACH IMAGE ##########
	nl.plotter(nbTests, title)
	
	input('Press Enter to quit...')

if __name__ == '__main__':
	main()
