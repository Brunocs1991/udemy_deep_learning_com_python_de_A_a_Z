import numpy as np


def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0


def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))


def tahmFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))


def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0


def linearFunction(soma):
    return soma


def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()


teste = stepFunction(30)
teste1 = stepFunction(-1)

teste2 = sigmoidFunction(0.358)

teste3 = tahmFunction(0.358)
teste4 = tahmFunction(-0.358)

teste5 = reluFunction(-0.358)
teste6 = reluFunction(0.358)

teste7 = linearFunction(0.358)
teste8 = linearFunction(-0.358)

valores = [7.0, 2.0, 1.3]
print(softmaxFunction(valores))
