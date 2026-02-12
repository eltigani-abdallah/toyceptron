
class Layer:
    def __init__(self, weights_list : list[list[float]], biases_list : list[float]):
        self.weights_list = weights_list
        self.biases_list = biases_list


    def forward(self, input_list : list[float]) -> float:
        
