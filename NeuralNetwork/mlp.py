''' Feel free to use numpy for matrix multiplication and
other neat features.
You can write some helper functions to
place some calculations outside the other functions
if you like to.
'''
import numpy as np
import random


#add a column to a numpy matrix
def addCol(m, val):
	(r,c) = m.shape
	col = val * np.ones((r,1))
	m = np.hstack((m,col))
	return m

class mlp:
	def __init__(self, inputs, targets, nhidden):
		self.beta = 1
		self.eta = 0.1

		self.hidden = np.zeros((inputs.shape[0], nhidden +1))
		self.outputs = np.zeros((targets.shape))

		self.weight = np.random.uniform(low= -1, high=1, size=(40+1, nhidden))
		self.weight2 = np.random.uniform(low= -1, high=1, size=(nhidden+1, 8))


		print 'To be implemented'

	def earlystopping(self, inputs, targets, valid, validtargets):

		inputs = addCol(inputs, -1)
		valid = addCol(valid, -1)

		oldError = 100003 #High values to run first loops
		newError = 100000
		cnt = 0
		while (oldError - newError) > 1:
			cnt += 1
			print cnt
			self.train(inputs, targets)
			self.forward(valid)
			oldError = newError
			newError = np.sum(0.5*(validtargets - self.outputs)**2)


	def train(self, inputs, targets, iterations=100):

		for x in range(iterations):
			self.forward(inputs)
			self.backpropogation(inputs, targets)


	def backpropogation(self, inputs, targets):
		updatew1 = np.zeros((np.shape(self.weight)))
		updatew2 = np.zeros((np.shape(self.weight2)))

		deltao, deltah = self.calculateError(targets)

		updatew1 = self.eta*(np.dot(np.transpose(inputs),deltah[:,:-1]))/inputs.shape[1]
		updatew2 = self.eta*(np.dot(np.transpose(self.hidden),deltao))/inputs.shape[1]

		self.weight -= updatew1
		self.weight2 -= updatew2


	def calculateError(self, targets):
		deltao = (self.outputs-targets)
		deltah = self.hidden*(1.0-self.hidden)*(np.dot(deltao,np.transpose(self.weight2))) 
		return deltao, deltah;

	def forward(self, inputs):

		self.hidden = np.dot(inputs, self.weight)
		self.hidden = 1.0/(1.0+np.exp(-self.beta*self.hidden))
		self.hidden = addCol(self.hidden, -1)
		self.outputs = np.dot(self.hidden, self.weight2)
		print self.weight2

	def confusion(self, inputs, targets):
		'''Confusion matrix'''
		
		#Legger til input som matcher mias noden
		inputs = addCol(inputs, -1)
		self.forward(inputs)
		outputs = np.argmax(self.outputs,1)
		targets = np.argmax(targets,1)
		matrix = np.zeros((8,8))
		for i in range(8):
			for j in range(8):
				matrix[i,j] = np.sum(np.where(outputs==i,1,0)*np.where(targets==j,1,0))

		print "Confusion matrix:"
		print matrix
		print "With: {:.2%} correct".format(np.trace(matrix)/np.sum(matrix) ,'d')