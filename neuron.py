import random

# created during live coding of Feb 12

class Neuron:
    """ a simple neuron, no AI generated code this time around"""

    def __init__(self, weights : list[float] = [], bias : float = 0.0, size : int = 0 ):
        if weights == []:
            self.weights = []
            for i in range (size):
                self.weights.append(random.uniform(-1,1))
        else:
            self.weights = weights
        self.bias = bias


    def forward(self, input_list : list[float]) -> float:
        """
        takes in a list of inputs, multiplies said list by the weights then adds the bias
        as discussed in the suivi of feb 11th
        """
        total = 0

        if len(input_list) != len(self.weights):
            raise ValueError("input list length is not equal to weights list length, you done goofed up")
        
        else:
            for i in range(len(input_list)):
                # print("input is: ", i)
                total+=input_list[i] * self.weights[i]

        total += self.bias
        return total
