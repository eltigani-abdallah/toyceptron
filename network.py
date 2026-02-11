from layer import Layer

class Network:
    def __init__(self, input_size, activation):
        # Taille du vecteur d'entrée
        self.input_size = input_size 
        self.activation = activation # Fonction d'activation utilisée après chaque couche
        self.layers = [] # Liste toutes les couches du réseau

    def add(self, weights, biases):
        # Ajout d'une nouvelle couche au réseau
        layer = Layer(weights, biases)
        self.layers.append(layer)

    def feedforward(self, inputs):
        # Propagation des données à travers toutes les couches
        for layer in self.layers:
            # Calcul des sorties brutes de la couche
            raw_outputs = layer.forward(inputs)

            # Application de la fonction d'activation
            inputs = [self.activation(o) for o in raw_outputs]

        # Sortie finale du réseau
        return inputs
    
#Network : représente tout le réseau de neurones
#add : permet d’ajouter des couches au réseau
#feedforward : fait passer les données de l’entrée jusqu’à la sortie
#la fonction d’activation est appliquée après chaque couche
