import numpy as np

np.random.seed(0)
# training sample of inputs
X = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):

        # change [neurons x inputs] -> [inputs x neurons] for <Transpose>
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons))      # first tuple - shape size

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)


"""
# training set of batches
inputs = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
]

# shape => [neurons x inputs] => 3 neurons on the output, 4 inputs
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]

# shape => [inputs x neurons] => 3 neurons on the output, 4 inputs
weights_t = [
    [ 0.2 ,  0.5 , -0.26],
    [ 0.8 , -0.91, -0.27],
    [-0.5 ,  0.26,  0.17],
    [ 1.  , -0.5 ,  0.87]
]

biases = [
    2, 3, 0.5
]

output = np.dot(inputs, np.array(weights).T) + biases
print(output)
"""