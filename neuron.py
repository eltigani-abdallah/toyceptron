# Un neurone représente une unité de calcul très simple
# Il reçoit des entrées, les multiplie par des poids et ajoute un biais

class Neuron:
    def __init__(self, weights, bias):
        # weights : importance de chaque entrée
        self.weights = weights
        # bias : valeur ajoutée pour décaler le résultat
        self.bias = bias

    def forward(self, inputs):
        # Calcul de la somme pondérée des entrées
        result = 0.0
        for w, x in zip(self.weights, inputs):
            result += w * x

        # Ajout du biais pour ajuster le résultat
        result += self.bias

        # On retourne la valeur brute (sans activation)
        return result

# Neuron : représente un neurone artificiel
#weights : importance de chaque entrée
#bias : permet de décaler le résultat
#forward : calcule la sortie du neurone à partir des entrées