from layer import Layer

class Network:
    def __init__(self, input_size : int, activation):
        self.input_size = input_size
        self.activation = activation
        self.layers = []


    def add(self, weights : list[list[float]], biases : list[float]):
        if len(weights) != len(biases):
            raise ValueError ("Weights list length does not match biases list length")
        
        self.layers.append(Layer(weights, biases))

    
    def activate(self,raw_layer_output : list[float]) -> list[float]:
        activated_list = []

        for item in raw_layer_output:
            activated_list.append(self.activation(item))


        return activated_list
    
    def feedforward(self,net_input : list[float]) -> list[float]:
        prev_layer_output = []
        current_layer_output = []


        for layer in self.layers:
            if prev_layer_output == []:
                current_layer_output = self.activate(layer.forward(net_input))
            else:
                current_layer_output = self.activate(layer.forward(prev_layer_output))
                
            prev_layer_output = current_layer_output
            




        return prev_layer_output
    


