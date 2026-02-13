import random

# created during live coding of Feb 12

class Neuron:


    def __init__(self, weights : list[float] = [], bias : float = 0.0, size : int = 0 ):
        if weights == []:
            self.weights = []
            for i in range (size):
                self.weights.append(random.uniform(-1,1))
        else:
            self.weights = weights

        self.bias = bias
        if size == 0:
            self.size = len(weights)



    def forward(self, input_list : list[float]) -> float:
        total = 0

        if len(input_list) != len(self.weights):
            print("-------------Neuron.forward--------------")
            for i in input_list:
                print(f"input item: {i} in position {input_list.index(i)}")
            print(f"input list len: {len(input_list)}")
            print(f"weights len: {len(self.weights)}")
            raise ValueError("input list length is not equal to weights list length, you done goofed up")
        
        else:
            for i in range(len(input_list)):
                # print("input is: ", i)
                total+=input_list[i] * self.weights[i]

        total += self.bias
        return total
