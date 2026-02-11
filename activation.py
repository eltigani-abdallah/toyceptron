# Fonctions d'activation simples

def act_identity(x):
    # La sortie est exactement la même que l'entrée
    return x

def act_threshold(x):
    # transforme une valeur en 0 ou 1
    if x > 0:
        return 1
    return 0

def act_relu(x):
    # ReLU (Rectified Linear Unit) : renvoie 0 si x est négatif
    # Sinon, la sortie est égale à la valeur d'entrée
    return max(0, x)

#Identité : ne change rien, utile pour des tests simples

#Seuil : transforme une valeur en 0 ou 1 selon qu'elle est négative ou positive

#ReLU : renvoie 0 si l'entrée est négative, sinon la même valeur que l'entrée
#ReLU : garde les valeurs positives et supprime les négatives