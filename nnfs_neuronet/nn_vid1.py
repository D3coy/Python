import sys
import numpy
import matplotlib

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)

"""
i[1.2]---------------
              w[3.1]  \
i[5.1]--------w[2.1]---[O]----->>> [output]
              w[8.7]  / |
i[2.1]----------------  |
                      b[3]

Prototype of one neuron with 3 inputs from previous layers and same amount of weights
"""