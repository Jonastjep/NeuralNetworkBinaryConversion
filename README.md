# NeuralNetworkBinaryConversion
Neural Network porject that teaches program to convert simple binary numbers to decimal

######################### HOW TO USE THIS PROGRAM #########################

INTRO:
This Neural Network learns to convert three* bit binary to decimal (so from
0 to 7). The library was designed to make it easy to create Neural networks
for other purposes and the basic structure of NeuralNetworkFinal.py is made
to be easily modified (adding layers, neurones, changing learning rate, etc...)
so that it can played with and test different combinations. The following 
list is to help you get started with this particular program that converts binary
to decimal. I'm aware this sort of conversion is not a particularly exciting, 
but this is more about the how than the what. Neural Networks are fascinating
and I hope you'll have as much fun as I did exploring all the different facettes
of this very simple neural network.

Just for your information, I haven't implemented stochastic gradient descent, so 
do not exagerate on the number of trainings you do.

*You can easily change this number to what ever you want directly from the program script
but do not forget to adapt the whole neural network to your change, particularly the input
and output layers that will have different nb of neurones.

STEPS

1.	You first have to use 'binaryFileCreator.py' to create a file named 'Test_File_NN.txt' 
	(or whatever name you want, you will just have to change the testFile variable in 
	NeuralNetworkFinal.py to match the name you chose !!Don't forget the .txt!!)
	You will have to choose a number which represents the number of trainings you want
	your network to go through.

	You will see that the first printed number is the number you entered in the cmd.
	This number is used as information on how many trainings the network will go 
	through, so choose wisely.
	The second and third line will look something like this:
			101	  --> three digit binary
			00000100  --> the supposed output of the program
	This last line actually represents each output neuron of the network and each of these
	neurons represent a decimal digit so here,
	00000100
	||||||||
	01234567
	--> output = 7
	And of course 101 is binary for 7.

2.	Just launch the main program and everything should work out fine! It will output the
	graph of the cost function at each iteration. Ideally your graph should tend to zero, but that
	all depends on your settings. I would encourage you to go and tweak the variables at the 
	begining of the code. You can change the learning rate and number of neurons in the hidden
	layer with no anxiety, and find the optimal settings for this task. 

	The NbNeur array represents each layer with it's number of neurons
	The NbLay represents the number of layers.

	The program creates two other files : 'CostFile.txt' and 'AnswerFile.txt'
	The first is used in the graphing function. It containes all the raw values of your individual
	Cost Function. You should see by scrawling it down that it goes towards 0, exactly as we want it.
	The second isn't used in the program (though it could be used to calculate efficiency percentage)
	and so is for the user only. Each row contains two digits: the first one shows what is the decimal
	value that the program has converted (can be wrong, depending on the number of iterations the 
	prog has run) and the second is what it should have been. As you scrawl down the file, the two numbers
	should more and more often be the same: the program is learning and making less faults.

This is it, this file will probably be updated in the future, with more info about the functions
and the rest of the program or it might be in a special function text file.

Cheers!
