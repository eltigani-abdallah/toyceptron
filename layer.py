from neuron import Neuron

class Layer:
    def __init__(self, weights_list : list[list[float]], biases_list : list[float]):
        self.weights_list = weights_list
        self.biases_list = biases_list
        self.neuron_list = []
        self.neuron_size = 0

        for neuron in self.neuron_list:
            if self.neuron_size != neuron.size:
                raise ValueError ("you have neurons of different sizes in the same layer \n what the heck")
            self.neuron_size = neuron.size

        for i in range(len(weights_list)):
            # print("-------------------Layer.init neuron creation-----------------------")
            # print(f"creating neuron with {self.weights_list[i]} weights \n {self.biases_list[i]} biases")
            self.neuron_list.append(Neuron(self.weights_list[i], self.biases_list[i]))


    def forward(self, input_list : list[float]) -> list[float]:
    
        
        layer_output = []
        for neuron in self.neuron_list:
            layer_output.append(neuron.forward(input_list))
        
        return layer_output
        
