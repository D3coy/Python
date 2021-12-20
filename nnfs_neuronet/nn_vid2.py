import sys
import numpy
import matplotlib
import ast
"""
Here we modeling three neurons with 4 inputs from previous layers (output layer basically)
"""

inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
outputs = []

output1 = inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1
output2 = inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2
output3 = inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3

gv = globals()
for i in range(1,4):
    # print(eval(f'\noutput{i}'))       # unsecure
    print("[output_neuron{}] -> {}".format(i, gv["output%d" % i]))
    outputs.append(gv["output%d" % i])

print(f"Full list of output neuron values -> {outputs}")
