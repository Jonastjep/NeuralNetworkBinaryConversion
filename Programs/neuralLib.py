import numpy as np
import matplotlib.pyplot as plt

############# SCALABLE WEIGHT MATRIX WITH RANDOM INPUT #################
def scalableWeightMatrix(nbLay, nbNeurone):
	#Fabrique la premiere couche de matrice [[],[],...]
	WM = []
	
	for i in range(nbLay-1):
		WM.append([])
	
	k=0
	
	#Fabrique la deuxieme couche de matrice [[[],[],[],...],[[],[],[],...],...]
	for i in range(nbLay-1):
		for j in range(nbNeurone[k+1]):
			WM[k].append([])
		k+=1
	
	k=0
	m=0
	
	#Fabrique la deuxieme couche de matrice [[[a,b,...],[a,b,...],[a,b,...],...],[[a,b,...],[a,b,...],[a,b,...],...],...]
	for i in range(nbLay-1):
		for j in range(nbNeurone[k+1]):
			for l in range(nbNeurone[k]):
				WM[k][m].append(round(np.random.uniform(0,1),1))
			m+=1
		k+=1
		m=0
	
	return WM
	
############## RETURNS MATRICES FOR Z AND B FILLED WITH 'FILL' #######################
def vector_Z_B_Err_Matrix(nbLay, nbNeur, fill):
	b = []
	for i in range(nbLay-1):
		b.append([])
		for j in range(nbNeur[i+1]):
			b[i].append(fill)
	return b

############## RETURNS MATRICES FOR A FILLED WITH 0. #######################
def vector_A_Matrix(nbLay, nbNeur):
	a = []
	for i in range(nbLay):
		a.append([])
		for j in range(nbNeur[i]):
			a[i].append(0.)
	return a

################ RETURNS VECTOR Y FOR WAITED VALUES ########################
def vector_Y_intended(nbLay, nbNeur, y):
	Y = []
	for i in range(nbNeur[nbLay-1]):
		Y.append(float(y[i]))
	return Y
	
################ FEEDFORWARD ########################
def feedforward(nbLay,nbNeur,W,B,A,Z):
	
	vectSigm = np.vectorize(sigmoid)
	
	for i in range(nbLay - 1):
		tempA = np.array(A[i]).reshape(len(A[i]),1)
		Z[i] = np.dot(W[i], tempA) + np.array(B[i]).reshape(len(B[i]),1)
		A[i+1] = vectSigm(Z[i])

################ SIGMOID FUNCTIONS ######################
def sigmoid(x):
	return 1/(1+np.exp(-x))
	
def sigmoidPrime(x):
	return np.exp(-x)/((np.exp(-x)+1)**2)

################ ERROR DELTA COMPUTATION, RETURNS INDIVIDUAL COST FUNC #################
def errorL(A,Y,Z,Err, nbLay, nbNeur):
	
	vectSigmPrime = np.vectorize(sigmoidPrime)

	CxArr = (np.subtract(A[len(A)-1], np.array(Y).reshape(len(Y),1)))
	
	Err[len(Err)-1] = np.multiply(CxArr, vectSigmPrime(Z[len(Z)-1]))
	Cx = 0
	
	for i in range(len(CxArr)):
		Cx += (CxArr[i][0]**2)
		
	return Cx
	
##################### ERROR BACKPROPAGATION #########################
def backpropError(W,A,Y,Z,Err, nbLay, nbNeur):
	vectSigmPrime = np.vectorize(sigmoidPrime)
	
	for i in range(nbLay-2):
		WT = np.array(W[i+1]).T  #Transpose of W
		Err[i] = np.multiply(np.dot(WT, Err[i+1]), vectSigmPrime(Z[i]))
	
###################### OUTPUT GRADIENT ##############################
def gradientOutput(Err, A, nbNeur, nbLay):
	A[0] = np.array(A[0]).reshape(len(A[0]),1)
	gradient = []
	
	############ FILL WITH Weight (W11, W21, W31, W12, W22,...) ###############
	for i in range(nbLay):
		if(i == nbLay-1):
			break
		for j in range(nbNeur[i+1]):
			for k in range(nbNeur[i]):
				gradient.append(A[i][k][0]*Err[i][j][0])
	
	#################### FILL WITH Bias #############################
	for i in range(nbLay-1):
		for j in range(nbNeur[i+1]):
			gradient.append(Err[i][j][0])
	
	return gradient
	
###################### GRADIENT DESCENT ##############################
def gradientDescent(W,B,gradient,learningRate, nbNeur, nbLay):
	
	grCount = 0			#notes the emplacement on the gradient array
	
	for i in range(nbLay-1):
		for j in range(nbNeur[i+1]):
			for k in range(nbNeur[i]):
				W[i][j][k] -= learningRate*gradient[grCount]
				grCount +=1
	
	for i in range(nbLay-1):
		for j in range(nbNeur[i+1]):
			B[i][j] -= learningRate*gradient[grCount]
			grCount +=1
	
####################### COST GRAPHING ################################
def plotter(nbTests, title):
	CostFile = open('CostFile.txt', 'r')
	
	cost = []
	
	for i in range(nbTests):
		cost.append(float(CostFile.readline().rstrip()))
	
	abscisse = np.arange(nbTests)
	
	plt.plot(abscisse,cost)
	
	plt.xlabel('Number of Training Images')
	plt.ylabel('Value of the cost function at each run')
	plt.title(title)
	plt.grid()
	plt.show()
	
	CostFile.close()

######################## PRINT ANSWER FILE ############################
#The answer file allows to see the output of the program and compare it to 
#the waited answer. As soon as the cost function value approaches 0, you
#should see a similar integer on the left and on the right
def AnswerFilePrintToTxt(A, AnswerFile, waitedNb, nbLay):
	MaxOutput = np.amax(A[nbLay-1])
	for i in range(len(A[nbLay-1])):
		if(A[nbLay-1][i][0] == MaxOutput):
			outputNb = i
		
	AnswerFile.write(str(outputNb))
	AnswerFile.write('\t')
	AnswerFile.write(str(waitedNb))
	AnswerFile.write('\n')


