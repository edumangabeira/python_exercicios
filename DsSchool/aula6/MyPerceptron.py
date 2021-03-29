import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron


class MyPerceptron:
	''' 
	Feito a partir de: https://github.com/python-engineer/MLfromscratch/
	e a partir do livro "Mãos à obra: aprendizado de máquina com ScikitLearn & TensorFlow" - Aurélien Géron.

	Atributos:
	learning_rate - taxa de aprendizado da rede neural.
	n_iters - número de iterações.
	heaviside - função de ativação.
	weights - pesos.
	bias - viés associado.

	Métodos:
	fit(x, y) - Ajusta modelo linear com gradiente descendente.
	predict(x) - Prediz rótulos de classe para amostras em x.
	heaviside(x) - implementa a função de ativação.
	'''
    
    def __init__(self, learning_rate = 0.01, n_iters = 1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.heaviside = self.heaviside
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        samples, features = x.shape
        self.weights = np.zeros(features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            
            for idx, x_i in enumerate(x):

                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.heaviside(linear_output)
                
                # Perceptron update rule
                update = self.learning_rate * (y_[idx] - y_predicted)

                self.weights += update * x_i
                self.bias += update

    def predict(self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        y_predicted = self.heaviside(linear_output)
        return y_predicted

    def heaviside(self, x):
        return np.where(x>=0, 1, 0)