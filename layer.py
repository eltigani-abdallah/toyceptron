# Une couche est un ensemble de neurones
# Tous les neurones reçoivent le même vecteur d'entrée

from neuron import Neuron

class Layer:
    def __init__(self, weights_list, biases_list):
        # Liste qui va contenir des neurones de la couche
        self.neurons = []

        # Création des neurones à partir des poids et des biais
        for weights, bias in zip(weights_list, biases_list):
            self.neurons.append(Neuron(weights, bias))

    def forward(self, inputs):
        # Applique les entrées à tous les neurones de la couche
        outputs = []
        for neuron in self.neurons:
        # Chaque neurone calcule sa sortie
            outputs.append(neuron.forward(inputs))

        # On retourne les sorties brutes de la couche
        return outputs
    
#Layer : représente une couche de neurones(groupe de neurones)
#__init__ : crée les neurones de la couche
#forward : envoie les entrées à chaque neurone et récupère leurs sorties
